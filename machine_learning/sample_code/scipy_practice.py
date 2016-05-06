import numpy as np
from scipy import sparse

# SciPy入門

a = sparse.lil_matrix((5,5))
# <5x5 sparse matrix of type '<class 'numpy.float64'>'
#  with 0 stored elements in LInked List format>

a[0,0] = 1
a[1,2] = 2
a[3,4] = 3
a[4,4] = 4

a.todense()
# matrix([[ 1.,  0.,  0.,  0.,  0.],
#         [ 0.,  0.,  2.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.,  3.],
#         [ 0.,  0.,  0.,  0.,  4.]])


b = a.tocsr()
# <5x5 sparse matrix of type '<class 'numpy.float64'>'
#  with 4 stored elements in Compressed Sparse Row format>

b.getrow(1).todense()
# matrix([[ 0.,  0.,  2.,  0.,  0.]])

v = np.array([1,2,3,4,5])
a.dot(v)
# array([  1.,   6.,   0.,  15.,  20.])
