@echo off
rem Build the next version of the CAD with nl-cad, which must be checked out at ..\nl-cad.
rem Usage: build.cmd "what changed"
setlocal
set "HERE=%~dp0"
set "PYTHONPATH=%HERE%..\nl-cad"
pushd "%HERE%"
uv run --project "%HERE%..\nl-cad" python -m nlcad.build projects/feed-pump --note "%~1"
popd
endlocal
