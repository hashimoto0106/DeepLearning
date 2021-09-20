# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:27:21 2020

@author: sample
"""


# クラスのコメント
class Fruit(object):
    """
    果物の各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    fruit_id : int
        対象の果物のマスタID。
    fruit_name : str
        果物名。
    price_dict : dict
        キーに地域のID、値に該当する地域での値段を保持した辞書。
    """

    def __init__(self, fruit_id):
        """
        Parameters
        ----------
        fruit_id : int
            対象の果物のマスタID。
        """
        self.fruit_id = fruit_id
        self.fruit_name = self.get_fruit_name(fruit_id=fruit_id)
        self.price_dict = self.get_price_dict(fruit_id=fruit_id)

    def get_fruit_name(self, fruit_id):
        # ...内容省略。
        pass

    def get_price_dict(self, fruit_id):
        # ...内容省略。
        pass
