# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 07:51:07 2020

@author: saito yoichiro
"""
"""
color_setA = {"blue", "yellow", "red"}
color_setB = {"green", "blue", "black"}
#print(len(color_setA))
print("red" in color_setA)
print("red" in color_setB)
print("red" not in color_setB)
"""
"""
num2set = set(range(0, 20 ,2))
num3set = set(range(0, 20, 3))
print(num2set)
print(num3set)
"""
"""
data = [101, 103, 103, 115, 167, 167, 189]
dataset = set(data)
#print(dataset)
datalist = list(dataset)
print(datalist)
datalist.sort()
print(datalist)
"""
"""
happyset = set("happy")
print(happyset)
"""
"""
fruits = set()
fruits.add("apple")
fruits.add("orange")
fruits.add("banana")
fruits.add("peach")
fruits.add("orange")
#print(fruits)
#fruits.remove("banana")
#print(fruits)
#fruits.remove("banana")
#print(fruits)
fruits.discard("lemon")
#print(fruits)
fruits.discard("orange")
#print(fruits)
#fruits.clear()
#print(fruits)
item = fruits.pop()
print(item)
print(fruits)
"""
"""
dataset = frozenset(["a", "b", "c"])
print(dataset)
print(type(dataset))
#dataset.add("x")
dataset.clear()
"""
"""
numbers = [1, 2, 3, 4, 5, 6]
num_set = {num * 2 for num in numbers}
print(num_set)
"""
"""
numbers = [-1.3, 1.2, -1.2, 1.1, 1.5, -1.1, 1.2, 1.1, 1.4]
num_set = {num for num in numbers if num>0}
print(num_set)
"""
"""
a = {"りんご", "みかん", "桃", "いちご"}
b = {"いちご", "スイカ", "みかん", "バナナ"}
#c = a | b
c = a & b
#print(c)
d = {"いちご", "スイカ"}
e = {"みかん", "バナナ"}
f = a | d | e
#print(f)
g = {"いちご", "りんご"}
#h = a & b & g
#print(h)
#h = a.intersection(b, g)
#print(h)
#i = a - b
#i = a.difference(b)
#print(i)
#j = a ^ b
j = a.symmetric_difference(b)
print(j)
"""
"""
set1 = {1, 2, 3}
list1 = [2, 4, 6, 8]
list2 = [3, 6, 9]
data = set1.union(list1, list2)
print(data)
"""
"""
data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}
#data.update(data2, data3)
#print(data)
data |= data2
data |= data3
print(data)
"""
"""
data = {"red", "blue", "green", "yellow"}
data2 = {"blue", "black", "yellow"}
#data.intersection_update(data2)
#data &= data2
#data.difference_update(data2)
#data -= data2
#data.symmetric_difference_update(data2)
data ^= data2
print(data)
"""
"""
a = {1, 2, 3}
b = {3, 2 ,1}
c = {1, 2, 3, 4}
#print(a == b)
#print(a == c)
print(a != b)
print(a != c)
"""
"""
a = {"earth", "wind", "fire"}
b = {"sky", "sea"}
c = {"fire", "water"}
print(a.isdisjoint(b))
print(a.isdisjoint(c))
"""

a = {"blue", "red"}
b = {"blue", "green", "red", "pink", "white"}
#print(a.issubset(b))
#print(a <= b)
print(b.issuperset(a))
print(b >= a)
