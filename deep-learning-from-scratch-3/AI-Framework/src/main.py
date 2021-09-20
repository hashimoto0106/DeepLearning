# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:18:02 2020

@author:sample
"""


import translation
import parameter
import function
import help
import version
import common.graph3d
import common.graph2d
import common.line
import common.console
import common.database
import common.logger
import config
import numpy as np
from datetime import datetime
from tqdm import tqdm
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# import common.rsyslog
# import common.syslog


def proc():
    # 2D Graph
    graph_2d = common.graph2d.graph("title", True)
    graph_2d.set_graph("xlabel", "ylabel", (-10, 10), (-10, 10))
    graph_2d.plot_vector("x", (0, 0), (3, 5), "blue")
    graph_2d.plot_vector("x", (0, 0), (1, 8), "green")
    graph_2d.plot_point("point", (4, 2), ".", "red")
    graph_2d.plot_circle((3, 2), 1, "yellow")
    graph_2d.plot_rectangle((-5, -5), 1, 3, "yellow")
#    graph_2d.plot_ellipse_test((-2.5, -2.5), 1, 3, "yellow")
    graph_2d.plot_ellipse("ellipse", (-2.5, -2.5), 1, 3, 45, "yellow")

    # Image Graph
    graph_image = common.graph2d.graph("Image", True)
    graph_image.set_graph_image(500, 480)
    graph_image.plot_point("point", (140, 300), ".", "red")

    # 3D Graph
    graph_3d = common.graph3d.graph(
        "title", "xlabel", "ylabel", "zlabel", (-10.0, 10.0), (-10.0, 10.0), (-10.0, 10.0), True)
    graph_3d.set_coodinate((0, 0, 0), (10, 0, 0), (0, 10, 0), (0, 0, 10))
    graph_3d.plot_vector("x", (0, 0, 0), (2, 5, 9), "blue")
    graph_3d.plot_vector("x", (0, 0, 0), (-1, -3, -4), "green")
    graph_3d.plot_point("point", (3, 7, -8), ".", "red")
    graph_3d.plot_sphere((1, 2, 3), 3, "red")
    graph_3d.plot_sphere((-1, -2, -3), 2, "yellow")

    # 極座標
    graph_polar = common.graph2d.graph("title", True, True)
    graph_polar.set_graph_polar(5)
    graph_polar.plot_point_polar("point", 2.0, 1.0, ".", "red")
    graph_polar.plot_point_polar("point", 1, 0.5, ".", "green")

    # 確率分布
#    graph_norm = graph2d.graph("norm", False)
#    mean = np.array([0.0, 0.0])  #2変数の平均値を指定
#    cov  = np.array([[5.0,1.0],[1.0,2.0]])  #2変数の分散共分散行列を指定
#    graph_norm.multivariate_normal(mean, cov)
#    graph_2d.plot_point("point", (4, 2), ".", "red")

    print(parameter.PARAMETER1)
    print(parameter.PARAMETER2)
    function.get_fruit_price(1, 0)
    for i in tqdm(range(10)):
        time.sleep(0.02)


if __name__ == "__main__":

    common.logger.app_logger.info(
        'Application Ver.%s Start', version.get_version())
    print(common.console.Fore.RED + "Red")
    print(common.console.Color.RED + "BLACK" + common.console.Color.END)
    # rsyslog.open()
    # rsyslog.logging(syslog.LOG_ALERT, 'Application started')
    now = datetime.now()
    start_time = time.time()

    os.system('cls')  # コンソールクリア
    # database.create_table()  # テーブル生成
    common.logger.logging_environment()  # 実行環境ログ
    config.logging_paramter()  # Parameter読み込み

    translation.init()
    print('*****************************This is sample message.')
    print('This string isn\'t translated.')
    print(common.console.Fore.RED + "Red")

    proc()

    # line.send_message("Application End")
    proc_time = (time.time()-start_time)
    common.database.insert(now, proc_time)  # データベース追加
    common.logger.app_logger.info('Application End(%.6lf[sec])', proc_time)
    print("foo," + common.console.Fore.BLUE +
          "bar," + common.console.Back.RED + "baz")
    # rsyslog.logging(syslog.LOG_ALERT, 'Application End')
    # rsyslog.close()
