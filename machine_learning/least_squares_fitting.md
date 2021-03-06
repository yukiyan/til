# 最小二乗法
回帰分析では、与えられたデータがどのような関数から生み出されたかという「関数関係」を推測することが目標。
最小二乗法は、回帰分析における基礎。  

## 概要
![img_0615](https://cloud.githubusercontent.com/assets/7304122/14403359/8b47f914-fe8e-11e5-893b-6dd13b6aca0c.png)

## 統計モデルとしての最小二乗法
統計モデル = 何らかの現象について、統計学的な手法を用いて、それを説明、あるいは、予測するモデル(数式)を作り出すこと

### パラメトリックモデル
アルゴリズムを組み立てていく上で、重要なガイドライン

1. パラメータを含むモデル(数式)を設定する
2. パラメータを評価する基準を定める
3. 最良の評価を与えるパラメータを決定する

### 判断基準
* 計算が簡単ということは、このモデルを数学的に分析して、その特徴を深く理解することが可能になる。
* 機械学習で得られた結果が、そのままビジネス判断に利用できるものではない。
* 使用するモデルの数学的な性質がよくわかっていれば、得られた結果の持つ意味を深く理解して、現実のビジネスに役立つ判断指標へとより適切に変換することが可能になる。

### オーバーフィッティングの検出
* 機械学習というのは、トレーニングセットとして与えられたデータに基づいて、最適なパラメータを決定する仕組み
* 得られた結果が「未来の値を予測する」ことに役立つかどうか
* 未知のデータに対する予測能力を「モデルの汎化能力」と呼ぶ。
* トレーニングセットだけが持つ特徴に合わせて、過剰なチューニングが行われている。 = 過学習(オーバーフィッティング)
* クロスバリデーション(交差検証)によって学習の効果を安定させる
