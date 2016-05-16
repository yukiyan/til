from sklearn import datasets
from sklearn import svm
from sklearn import cross_validation

# データの読み込み
iris = datasets.load_iris()

# 学習
svc = svm.SVC()
scores = cross_validation.cross_val_score(svc, iris.data, iris.target, cv=5)

print(scores)
print("Accuracy:", scores.mean())
