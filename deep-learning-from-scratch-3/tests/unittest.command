#!/bin/bash
cd `dirname $0`
python -m unittest discover ./ -v > unittest_result.log
