import numpy as np

"""
a = np.array([1, 2.5, 3])
print(a)
data = (True, False, "3")
b = np.array(data)
print(b)
c = np.array(data, dtype=int)
print(c)
d = np.array([9.123, 10.5, 12.11], dtype="<U4")
print(d)
"""
"""
#a = np.array([[1, 2, 3], [4, 5, 6]])
#print(a)
line1 = [10, 20, 30]
line2 = [40, 50, 60]
line3 = [70, 80, 90]
a = np.array([line1, line2, line3])
print(a)
"""
"""
data = [1, 2, 3, 4, 5, 6]
a = np.array(data)
print(a)
a = a.reshape(2, 3)
print(a)
"""
"""
a = np.array([[0, 1], [2, 3], [4, 5]])
print(a.ravel())
print(a.flatten())
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
"""
"""
a = np.array([0, 1, 2])
b = np.append(a, 3)
print(a)
print(b)
c = np.append(a, [3, 4, 5])
print(c)
"""
"""
a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(a)
b = np.append(a, [[7, 8, 9]], axis=0)
print(b)
"""
"""
a = np.array([0, 1, 2])
b = np.insert(a, 1, 99)
print(a)
print(b)
c = np.insert(a, 1, [88, 99])
print(c)
"""
"""
words = np.array(["dog", "cat", "bird"])
#new_words = np.insert(words, 0, "snake")
new_words = np.delete(words, len(words)-1)
print(new_words)
"""
"""
a = np.array([[0, 1], [2, 3], [4, 5]])
print(a)
print(np.transpose(a))
print(a.T)
"""
"""
data = [1, 2, 3, 4, 5, 6]
a = np.array(data)
b = a[:, np.newaxis]
print(b)
"""

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[0, 1], [2, 3], [4, 5]])
print(a.tolist())
print(b.tolist())
