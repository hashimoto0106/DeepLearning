pushd %~dp0
pylint --rcfile=./pylintrc ../../src ../../src/common > pylint_result.log
pause
