import numpy as np
import matplotlib.pyplot as plt

# 折れ線グラフ
x = [1,2,3,4]
y = [3,5,4,7]

plt.plot(x,y)
# [<matplotlib.lines.Line2D object at 0x10f73ec50>]

plt.show()


# 曲線の描画
x = np.linspace(-5,5,100)
y = x**2

plt.plot(x,y)
# [<matplotlib.lines.Line2D object at 0x11050fa58>]

plt.show()

# 散布図
x = [1,2,3,4]
y = [3,5,4,7]

plt.scatter(x,y)
# <matplotlib.collections.PathCollection object at 0x110583978>

plt.show()

# 複数系列を含む散布図(カラー)
x = np.array([1,2,3])
y1 = np.array([2,3,4])
y2 = np.array([7,6,5])

plt.scatter(x,y1,c="b")

plt.scatter(x,y2,c="r")

plt.show()

# 複数系列を含む散布図(白黒)
x = np.array([1,2,3])
y1 = np.array([2,3,4])
y2 = np.array([7,6,5])

plt.scatter(x,y1,marker="o",c="k")

plt.scatter(x,y2,marker="+",c="k")

plt.show()
