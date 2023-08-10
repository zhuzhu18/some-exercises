import numpy as np

def C(u, N):
    if u == 0:
        return np.sqrt(1/N)
    else:
        return np.sqrt(2/N)

def get_transform_matrix(N):
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            A[i][j] = C(i, N) * np.cos((j+0.5)*np.pi*i/N)
    return A

N = 8      # 块大小
x = np.random.rand(N, N)
A = get_transform_matrix((N))
F = A @ x @ A.T      # 正变换
print(F)          # 手动实现dct变换后的频谱系数与cv2.dct实现的结果一致
print(A.T @ F @ A)      # 逆变换


import cv2
y = cv2.dct(x)       # 直接调用opencv的dct变换
print(y)
print(cv2.idct(y))
