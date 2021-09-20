pushd %~dp0
mypy ../../src ../../src/common > mypy_result.log
pause
