pushd %~dp0
radon cc ../../src ../../src/common > radon_cc_result.log
radon raw ../../src ../../src/common > radon_raw_result.log
radon mi ../../src ../../src/common > radon_mi_result.log
radon hal ../../src ../../src/common > radon_hal_result.log
pause
