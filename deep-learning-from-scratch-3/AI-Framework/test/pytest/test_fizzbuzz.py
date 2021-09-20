# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:07:38 2020

@author: PC
"""

import pytest
import sys
sys.path.append('../../src')
import fizzbuzz as fb


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_normal(self):
    	assert fb.fizzbuzz(1) == 1

    def test_fizz(self):
    	assert fb.fizzbuzz(3) == "Fizz"

    def test_buzz(self):
    	assert fb.fizzbuzz(5) == "Buzz"

    def test_fizzbuzz(self):
    	assert fb.fizzbuzz(15) == "FizzBuzz"


if __name__ == "__main__":
    unittest.main()
