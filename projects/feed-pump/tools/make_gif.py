"""Render a build in OK Studio style and make its looping GIF. Needs ..\\nl-cad\\local.toml for the Blender path, plus ffmpeg on PATH.

    uv run --no-project --with pillow python projects/feed-pump/tools/make_gif.py projects/feed-pump/builds/vN

Writes renders/ok_*_vN.jpg and feed-pump_vN.gif into the build. Theme values are from okstudio-style tokens.json, dark mode.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
NLCAD = REPO.parent / "nl-cad"
FONT = REPO.parent / "okstudio-style" / "fonts" / "RobotoMono-500.ttf"
INK, MUTED, RULE, ACCENT = "#e2ecf5", "#7f93a8", "#2c3b50", "#35c4d7"     # tokens.json mode.dark: ink, muted, border, accent


def main(build):
    build = Path(build).resolve()
    n = build.name[1:]
    blender = tomllib.loads((NLCAD / "local.toml").read_text(encoding="utf-8"))["tools"]["blender"]
    stills = build / "renders"
    stills.mkdir(exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="feedpump_gif_"))
    try:
        r = subprocess.run([blender, "-b", "-P", str(HERE / "render_ok.py"), "--", str(build / f"feed-pump_v{n}.glb"),
                            str(build / f"manifest_v{n}.json"), str(stills), str(work), n], capture_output=True, text=True)
        if r.returncode != 0 or not (work / "captions.json").exists():
            print(r.stdout[-2500:], r.stderr[-1500:])
            raise SystemExit("blender render failed")

        captions = json.loads((work / "captions.json").read_text(encoding="utf-8"))
        font = ImageFont.truetype(str(FONT), 13)
        for f, cap in enumerate(captions):
            p = work / f"f{f:04d}.png"
            im = Image.open(p).convert("RGB")
            d = ImageDraw.Draw(im)
            d.line((20, im.height - 44, im.width - 20, im.height - 44), fill=RULE)
            d.text((20, im.height - 34), cap, font=font, fill=ACCENT if cap == "RUNNING" else INK)
            note = f"CONCEPT CAD V{n}. NOT A MEDICAL DEVICE"
            d.text((im.width - 20 - d.textlength(note, font=font), im.height - 34), note, font=font, fill=MUTED)
            im.save(p)

        out = build / f"feed-pump_v{n}.gif"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "15", "-i", str(work / "f%04d.png"), "-vf",
                        "split[a][b];[a]palettegen=max_colors=96:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle",
                        "-loop", "0", str(out)], check=True)
        print(out, f"{out.stat().st_size / 1e6:.1f} MB")
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main(sys.argv[1])
