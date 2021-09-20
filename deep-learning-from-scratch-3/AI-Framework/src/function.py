# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:27:59 2020

@author: sample
"""

import sys
import common.logger


# 関数のコメント
def get_fruit_price(fruit_id, location_id):
    """
    果物の値段を取得する。

    Parameters
    ----------
    fruit_id : int
        対象の果物のマスタID。
    location_id : int
        対象地域のマスタID。

    Returns
    -------
    fruit_price : int
        対象の果物の値段。
    consumption_tax : int
        消費税値。
    """
    fruit_price = 0
    consumption_tax = 0

    try:
        # 処理
        fruit_price = fruit_id / location_id
        consumption_tax = fruit_id / location_id
    except:
        type, value, traceback = sys.exc_info()
        common.logger.app_logger.error('Except:%s<%s>%s', type, value, traceback)

    # ...関数内容省略。
    return fruit_price, consumption_tax
