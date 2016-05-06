import numpy as np

# NumPy入門

# 行列の設定

a = np.array([[1,2], [3,4]])
print(a)
# [[1 2]
#  [3 4]]

b = np.array(np.arange(10))
print(b)
# [0 1 2 3 4 5 6 7 8 9]

c = b.reshape(2,5)
print(c)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

# 行列の演算

a = np.arange(4).reshape(2,2)
print(a)
# [[0 1]
#  [2 3]]

b = np.arange(3,7).reshape(2,2)
print(b)
# [[3 4]
#  [5 6]]

print(a+b)
# [[3 5]
#  [7 9]]

print(a.T)
# [[0 2]
#  [1 3]]

print(a.T+b)
# [[3 6]
#  [6 9]]

print(a-b)
# [[-3 -3]
#  [-3 -3]]

print(np.dot(a,b))
# [[ 5  6]
#  [21 26]]

v = np.array([10,20])
print(np.dot(a,v))
# [20 80]

print(np.dot(v,a))
# [40 70]


# 配列操作

v = np.arange(10,15)
print(v)
# [10 11 12 13 14]

print(v[2:4])
# [12 13]

print(v[:3])
# [10 11 12]

print(v[3:])
# [13 14]

print(v[:-1])
# [10 11 12 13]

a = np.arange(1,5).reshape(2,2)
print(a)
# [[1 2]
#  [3 4]]

u = a[:,1]
print(u)
# [2 4]

ii = np.array([2,3])
print(v[ii])
# [12 13]

w = np.array([False, False, False, True, True])
print(v[w])
# [13 14]

print(a*2)
# [[2 4]
#  [6 8]]

print(np.exp(a))
# [[  2.71828183   7.3890561 ]
#  [ 20.08553692  54.59815003]]

print(v<13)
# [ True  True  True False False]

print(v[v<13])
# [10 11 12]

# 行列の結合

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
# [[0 1 2]
#  [3 4 5]]

print(b)
# [[ 6  7  8]
#  [ 9 10 11]]

print(np.c_[a,b])
# [[ 0  1  2  6  7  8]
#  [ 3  4  5  9 10 11]]

print(np.r_[a,b])
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

c = np.arange(3)
d = np.arange(3,6)

print(c)
# [0 1 2]

print(d)
# [3 4 5]

print(np.c_[c,d])
# [[0 3]
#  [1 4]
#  [2 5]]

print(np.r_[c,d])
# [0 1 2 3 4 5]
