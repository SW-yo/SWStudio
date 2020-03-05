# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:49:34 2020

@author: saitouyouichirou
"""
import numpy as np

"""
a = np.arange(10)
print(a)

"""
"""
n = 3
m = 4
b = np.arange(n*m).reshape(n, m)
print(b)
"""
"""
c = np.arange(10, 20, 2)
print(c)
"""
"""
d = np.arange(10, step = 0.5)
print(d)
"""
"""
A = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
B = np.array([1, 2, 9, 4, 8, 6]).reshape(2, 3)
C = (A == B)
print(C)
n = (A != B).sum()
print(n)
"""
"""
e = np.linspace(0, 120, 16)
print(e)
"""
"""
Data = np.empty((3, 2), dtype=int)
print(Data)
"""
"""
#E = np.identity(4)
E = np.identity(4, dtype=int)
print(E)
ZERO = np.zeros(9, dtype=int)
print(ZERO)
#ONE = np.ones(10)
ONE = np.ones((2, 3), dtype=int)
print(ONE)
"""
"""
data = np.array([1, 2, 3])
print(data.repeat(3).reshape((3, 3)))
"""
"""
data = np.arange(6).reshape(2, 3)
print(data)
print(data.repeat(2, axis=0))
print(data.repeat(2, axis=1))
"""
import matplotlib.pyplot as plt
"""
X = np.random.rand(100)
Y = np.random.rand(100)
plt.scatter(X, Y)
plt.show()
"""
"""
sigma = 2.5
mu = 50
#data = sigma * np.random.randn(2, 3) + mu
#data = np.random.binomial(n=100, p=0.1, size=(2, 3))
data = np.random.poisson(lam=10, size=(10))
print(data)
"""
"""
#ポアゾン分布（平均50、1000個）
data = np.random.poisson(lam=50, size=1000)
count, bins_edge, patches = plt.hist(data, bins = 100)
plt.grid()
plt.show()
"""
"""
np.random.seed(10)
f = np.random.rand(3)
print(f)
np.random.seed(10)
g = np.random.rand(3)
print(g)
"""
"""
data = np.arange(9).reshape(3, 3)
np.random.shuffle(data)
print(data)
"""
"""
data = np.loadtxt("./data/data.csv", delimiter=",", skiprows=1)
print(data)
"""

import pandas as pd
df = pd.read_csv("./data/data.csv")
header = df.columns.values
data = df.values
print(header)
print(data)
