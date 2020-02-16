# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:52:09 2020

@author: saito yoichiro
"""

"""
abc = ["a", "b", "c"]
xyz = ["x", "y", "z"]
ax = abc + xyz
print(ax)
"""

"""
colors = []
colors += ["red"]
colors += ["white", "black"]
print(colors)
"""

"""
data = [1, 3, 5]
newdata = [2, 4, 6]
data.extend(newdata)
print(data)
"""

"""
data = [1, 3, 5]
newdata = [2, 4, 6]
data.append(newdata)
print(data)
"""

"""
colors = ["blue", "red", "green", "yellow", "pink", "black", "white"]
#print(colors)
#print(colors[3:])
#print(colors[:3])
#print(colors[3:6])
print(colors[-1:])
print(colors[-2:])
print(colors[-2:-1])
print(colors[:-1])
"""

"""
data = [10, 21, 35, 49, 51, 60, 77, 81, 92, 100]
n = 3
data1 = data[:n]
data2 = data[n:]
#print(data1)
#print(data2)
data3 = data[::2]
data4 = data[1::2]
#print(data3)
#print(data4)
data5 = data[1:5][::2]
data6 = data[::2][1:5]
data7 = data[1:5:2]
#print(data5)
#print(data6)
#print(data7)
data8 = data[::-1]
data9 = data[::-2]
data10 = data[:-1][::-2]
print(data8)
print(data9)
print(data10)
"""

"""
colors_a = ["green", "blue", "red"]
colors_b = ["green", "blue", "red"]
colors_c = ["green", "red", "blue"]
#print(colors_a == colors_b)
#print(colors_a == colors_c)
#colors_a.append("white")
#print(colors_a)
#print(colors_b)
colors_d = colors_a
#print(colors_d)
#print(colors_a == colors_d)
colors_a.append("white")
print(colors_a)
print(colors_d)
"""


"""
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
#print(list_a is list_b)
#print(list_a is list_c)
#print(list_a is not list_c)
list_a[0] = 99
#print(list_a)
#print(list_b)
list_b[1] = 100
print(list_b)
print(list_a)
"""


"""
list1 = [10, 20, 30]
list2 = list1
list1 = [11, 22, 33]
print(list2)
"""

"""
num_a = 10
num_b = num_a
print(num_b)
print(num_a is num_b)
str_a = "こんにちは"
str_b = str_a
print(str_b)
print(str_a is str_b)
"""


list_mother = [10, 20, 30, 40, 50]
#list_work = list_mother.copy()
#print(list_work)
#print(list_mother is list_work)
#list_work[0] = 99
#print(list_work)
#print(list_mother)
#list_work = list_mother[:]
#print(list_work)
#print(list_mother is list_work)
list_work = list(list_mother)
print(list_work)
print(list_mother is list_work)