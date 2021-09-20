pushd %~dp0
coverage run test_fizzbuzz.py
coverage report -m > coverage.log
coverage html
pause
