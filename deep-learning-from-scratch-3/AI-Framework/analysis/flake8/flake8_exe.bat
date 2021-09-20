pushd %~dp0
flake8 --show-source ../../src ../../src/common > flake8_result.log
pause
