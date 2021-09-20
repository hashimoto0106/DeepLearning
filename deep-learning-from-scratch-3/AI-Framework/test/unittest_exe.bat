pushd %~dp0
python -m unittest test_fizzbuzz.py -v >unittest_result.log
pause
