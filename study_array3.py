# -*- coding: utf-8 -*-
import numpy as np
"""
A = np.array([10, 20, 30, 40]).reshape(2, 2)
print(A)
B = A + 5
print(B)
C = A - 5
D = A * 2
E = A / 2
print(C)
print(D)
print(E)
"""
"""
p0 = np.array([1, 1])
p1 = np.array([6, 4])
A = p1 - p0
print(A)
a_norm = np.linalg.norm(A)
print(a_norm)
A2 = A * 2
a2_norm = np.linalg.norm(A2)
print(a2_norm)
"""

A = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
"""
print(A)
#print(A.sum())
#print(A.sum(0))
#print(A.sum(1))
print(A.max())
print(A.max(0))
print(A.max(1))
print(A.min())
print(A.min(0))
print(A.min(1))
print(A.mean())
print(A.mean(0))
print(A.mean(1))
"""
"""
print(np.sum(A))
print(np.max(A, 1))
"""
"""
sigma = 3.5
mu = 65
#点数サンプルデータ（正規分布の乱数で作成する）
data = sigma * np.random.randn(200) + mu
x = float(input("得点は？："))
t_score = 10 * (x - data.mean()) / data.std() + 50
print("平均点：", round(data.mean(), 1))
print("標準偏差：", round(data.std(), 1))
print("偏差値：", round(t_score, 1))
"""
"""
A = np.array([4, 6, 3, 1, 7, 3])
B = (A > 5)
print(B)
"""
"""
A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([10, 20, 30, 40]).reshape(2, 2)
C = A + B
print(C)
D = A * B
E = A / B
print(D)
print(E)
"""
"""
A = np.array([5, 3])
B = np.array([4, -2])
C = A + B
print(C)
C = A - B
print(C)
"""
"""
A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([100, 200])
C = A + B
print(C)
"""
"""
A = np.array([1, 2, 3 ,4, 5, 6]).reshape(2, 3)
B = np.array([10, 20]).reshape(2, 1)
C = A + B
print(C)
"""
"""
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)
print(C)
"""
"""
F = np.array([8.66, 5.0])
S = np.array([20, 0])
W = np.dot(F, S)
print(W)
f = np.linalg.norm(F)
s = np.linalg.norm(S)
rad = np.radians(30)
w = f * s * np.cos(rad)
print(w)
"""
"""
a = np.array([1, 2, 0])
b = np.array([0, 1, -1])
c = np.cross(a, b)
print(c)
"""
"""
import math
data = [0.0, 0.28, 0.57, 0.85, 1.14, 1.42, 1.71, 1.99, 2.28, 2.57, 2.85, 3.14]
#print(math.sin(data))
print(np.sin(data))
"""

import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 180)
Y = np.sin(X)
plt.plot(X, Y)
plt.show()
