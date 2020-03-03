import numpy as np
"""
a = np.array([10, 20, 30, 40, 50, 60])
print(a[0])
print(a[1])
print(a[-1])
a[2] = 99
print(a)
"""
"""
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = np.array(data).reshape(3, 3)
print(a)
print(a[0, 0])
print(a[1, 0])
print(a[1, 1])
print(a[2, -1])
"""
"""
a = np.array([10, 20, 30, 40])
b = a.reshape(2, 2)
#print(a)
#print(b)
print(a is b)
b[0, 0] = 99
print(b)
print(a)
"""
"""
data = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
print(data[:])
print(data[:4])
print(data[4:])
print(data[3:7])
print(data[::2])
print(data[::-1])
"""
"""
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = np.array(data).reshape(3, 3)
print(a)
print(a[:2,])
print(a[:, 1:])
print(a[1:, 1:])
"""
"""
data = [2.1, 3.5, 2.5, 4.3, 5.1, 1.6]
a = np.array(data).reshape(3, 2)
print(a)
a2 = a[:2, ].astype(int)
print(a2)
"""
"""
data = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
for item in data:
    print(item)
"""
"""
words = ["flower", "bird", "wind", "moon"]
for i, item in enumerate(words, 1):
    print(i, item)
"""
"""
data = np.array([ 10, 20, 30, 40, 50, 60]).reshape(2, 3)
print(data)
for i, item in np.ndenumerate(data):
    print(i, item)
"""

a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8 ,9, 7, 9, 3])
#print(a[a>=5])
#print(a[a%2 == 0])
#print(a[a%2 == 1])
#b = a.reshape(4, 4)
#print(b)
#print(b[b>5])
#print(a[(a>=5) & (a%2 == 1)])
#print(a[(a%2 == 0) | (a%3 == 0)])
#print(a[~(a%3 == 0)])
#a = a.reshape(4, 4)
#a[a%2 == 0] = 0
#print(a)
#a[a%2 == 1] = 1
#print(a)
#a.sort()
#print(a)
a_decend = np.sort(a)[::-1]
print(a_decend)
"""
a = np.sort([4, 6, 3, 9, 1, 2, 5])
print(a)
"""
