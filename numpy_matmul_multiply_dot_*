import numpy as np

a = np.array([[1,2],[3,4]])       # 维度:(2,2)
b = np.array([[1,3],[2,4]])

c = np.array([1,2])               # 维度:(2,)

print(np.matmul(a, b))      # 矩阵乘法,得到的是[[ 5 11], [11 25]]
'''
如果维数不一致,则将一维数组与二维数组的每一行做内积,得到的是一维数组
不存在广播机制
'''
print(np.matmul(a, b))        # 得到的是[ 5 11]
print(np.matmul(a, c))          # 做内积运算,与matmul的作用相同,不存在广播机制
print(a.dot(c))

print(a*c)         # 对应元素相乘,[[ 1  6], [ 6 16]],存在广播机制
print(np.multiply(a, c))      # 也是对应元素相乘,[[ 1  6], [ 6 16]],存在广播机制
