import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

# データの読み込み
diabates = datasets.load_diabetes()

# データを訓練用と評価用に分ける
data_train   = diabates.data[:-20]
target_train = diabates.target[:-20]
data_test    = diabates.data[-20:]
target_test  = diabates.target[-20:]

# 学習させる
lin = linear_model.LinearRegression()
lin.fit(data_train, target_train)

# 当てはまり度合いを表示
print("Score :", lin.score(data_test, target_test))

# 最初の評価用データについて結果を予想して、実際の値と並べて表示
print("Prediction :", lin.predict(data_test[0]))
print("Actual value :", target_test[0])
