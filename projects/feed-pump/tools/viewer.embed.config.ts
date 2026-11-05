/*
 * Single-file offline viewer for a feed-pump build, themed with okstudio-style. Nothing is written inside nl-cad.
 *
 * nl-cad's own `pnpm export-html` reads only nl-cad/projects and uses the alex-style tokens it vendors. This config does the same
 * single-file build (plugin adapted from nl-cad/viewer/vite.embed.config.ts) from this project's build folder, and aliases
 * nl-cad's `../vendor/alex-style/*` imports to okstudio-style's web/ folder (same class and file names). Theme source:
 * okstudio-style commit 6fc4df7 (github owenpkent/okstudio-style).
 *
 * Run from the repo root (Git Bash), N = build number:
 *   NLCAD_DIR=W:/dev/nl-cad OKSTUDIO_DIR=W:/dev/okstudio-style EXPORT_VERSION=N EXPORT_OUT=<scratch folder> \
 *   node W:/dev/nl-cad/viewer/node_modules/vite/bin/vite.js build --config projects/feed-pump/tools/viewer.embed.config.ts
 * then copy <scratch folder>/dist/embedded.html to projects/feed-pump/builds/vN/feed-pump_viewer_vN.html (gitignored).
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const nl = process.env.NLCAD_DIR ?? "W:/dev/nl-cad";
const ok = process.env.OKSTUDIO_DIR ?? "W:/dev/okstudio-style";
const viewer = path.join(nl, "viewer");
const projectDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const project = "feed-pump";
const version = Number(process.env.EXPORT_VERSION ?? 0);
const out = process.env.EXPORT_OUT ?? path.join(os.tmpdir(), "feed-pump-viewer");

// vite and the single-file plugin come from nl-cad's own node_modules, so this file needs no install.
const load = async (rel: string) => import(pathToFileURL(path.join(viewer, "node_modules", rel)).href);

const safeJson = (v: unknown) => JSON.stringify(v).replace(/</g, "\\u003c");

function inlineBuildData() {
  return {
    name: "feed-pump-inline-build",
    enforce: "pre" as const,
    transformIndexHtml(html: string) {
      const dir = path.join(projectDir, "builds", `v${version}`);
      const read = (name: string) => { const f = path.join(dir, name); return fs.existsSync(f) ? fs.readFileSync(f) : null; };
      const manifest = read(`manifest_v${version}.json`);
      const glb = read(`${project}_v${version}.glb`);
      if (!manifest) throw new Error(`no manifest in ${dir}`);
      if (!glb) throw new Error(`no GLB in ${dir}`);
      const idx = JSON.parse(fs.readFileSync(path.join(projectDir, "builds", "index.json"), "utf8"));
      const entry = idx.filter((b: { version: number }) => b.version === version);
      const checks = read(`checks_v${version}.json`);
      const bom = read(`bom_v${version}.csv`);
      const data = {
        project, version, builds: entry.length ? entry : [{ version }],
        manifest: JSON.parse(manifest.toString("utf8")),
        checks: checks ? JSON.parse(checks.toString("utf8")) : null,
        bom_csv: bom ? bom.toString("utf8") : null,
      };
      const block = `<script type="application/json" id="nlcad-data">${safeJson(data)}</script>\n` +
        `<script type="application/octet-stream" id="nlcad-glb">${glb.toString("base64")}</script>`;
      return html.replace("<!-- nlcad-data -->", () => block)
        .replace("<title>nl-cad assembly viewer</title>", `<title>${project} v${version} assembly viewer</title>`);
    },
  };
}

// An async config function: vite bundles this file as CommonJS, which has no top-level await.
export default async () => {
  const { viteSingleFile } = await load("vite-plugin-singlefile/dist/esm/index.js");
  return {
    root: viewer,
    cacheDir: path.join(out, "cache"),
    plugins: [inlineBuildData(), viteSingleFile()],
    resolve: { alias: [{ find: /^\.\.\/vendor\/alex-style\/(.*)$/, replacement: path.join(ok, "web", "$1").split(path.sep).join("/") }] },
    define: { __EMBEDDED__: true },
    build: { outDir: path.join(out, "dist"), emptyOutDir: true, rollupOptions: { input: path.join(viewer, "embedded.html") }, chunkSizeWarningLimit: 4000 },
    logLevel: "warn" as const,
  };
};
