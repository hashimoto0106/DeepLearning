pushd %~dp0
autopep8 -i ../../src/main.py ../../src/main.py ../../src/class.py ../../src/config.py ../../src/fizzbuzz.py > autopep8_result.log
pause
