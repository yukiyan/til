import numpy as np
import matplotlib.pyplot as plt

# 等高線の可視化

# 描画に必要な関数
x = np.array([1,2,3])
y = np.array([4,5,6])
X,Y = np.meshgrid(x,y)

X
# array([[1, 2, 3],
#        [1, 2, 3],
#        [1, 2, 3]])

Y
# array([[4, 4, 4],
#        [5, 5, 5],
#        [6, 6, 6]])

X.ravel()
# array([1, 2, 3, 1, 2, 3, 1, 2, 3])

Y.ravel()
# array([4, 4, 4, 5, 5, 5, 6, 6, 6])

# 平面の塗り分け

x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)

X,Y = np.meshgrid(x,y)
Z = X.ravel()**2-Y.ravel()**2

plt.contourf(X,Y,Z.reshape(X.shape))
plt.show()

# 色の指定

x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)

X,Y = np.meshgrid(x,y)
Z = X.ravel()**2-Y.ravel()**2

plt.contourf(X,Y,Z.reshape(X.shape),levels=[-20,-10,0,10,20],colors=["r","g","b","y"])
plt.show()

# 等高線の描画

x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)

X,Y = np.meshgrid(x,y)
Z = X.ravel()**2-Y.ravel()**2

plt.contour(X,Y,Z.reshape(X.shape),colors="k")
plt.show()
