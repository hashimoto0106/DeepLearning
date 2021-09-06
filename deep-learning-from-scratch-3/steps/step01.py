import numpy as np

# 機械学習のシステムはデ、基礎とするータ構造に「多次元配列」を使用する。
# VariableクラスはNumpyの多次元配列のみを扱える仕様とする
class Variable:
    def __init__(self, data):
        self.data = data


data = np.array(1.0)
x = Variable(data)
print(x.data)

x.data = np.array(2.0)
print(x.data)