import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

# データの読み込み
iris = datasets.load_iris()

# 種類が2であるものを捨てる
data   = iris.data[iris.target != 2]
target = iris.target[iris.target != 2]

# ロジスティック回帰による学習とクロスバリデーションによる評価
logi = LogisticRegression()
scores = cross_validation.cross_val_score(logi, data, target, cv=5)

print(scores)
