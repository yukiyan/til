import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

# scikit-learn入門

# 線形回帰

# 乱数によりデータを生成
np.random.seed(0)
regdata = datasets.make_regression(100, 1, noise=20.0)

# 学習を行いモデルのパラメータを表示
lin = linear_model.LinearRegression()
lin.fit(regdata[0], regdata[1])
print("coef and intercept :", lin.coef_, lin.intercept_)
print("score: ", lin.score(regdata[0], regdata[1]))

# グラフを描画
xr = [-2.5, 2.5]
plt.plot(xr, lin.coef_ * xr + lin.intercept_)
plt.scatter(regdata[0], regdata[1])

plt.show()
