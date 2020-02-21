"""
colors = ("green", "red", "blue", "yellow")
#print(colors[0])
#print(colors[1])
#print(colors[-1])
#colors[1] = "orange"
#for item in colors:
#    print(item)
for i, item in enumerate(colors, 1):
    print(i, item)
"""

"""
(a, b) = (100, 200)
#[a, b] = [100, 200]
print(a)
print(b)
"""

"""
data = (12, 15)
(boy, girl) = data
print(boy)
print(girl)
"""

"""
numbers = (4, 8, 15, 16, 23, 42)
num = int(input("受験番号を入れてください："))
if num in numbers:
    print("合格です")
else:
    print("不合格です")
"""

"""
data = (56, 45, 83, 67, 59, 41, 77)
print(sum(data))
print(max(data))
print(min(data))
"""

"""
a =(1, 2, 3)
b = a
c = (1, 2, 3)
print(a == b)
print(a is b)
print(a == c)
print(a is c)
"""

"""
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
zip_obj = zip(x, y, z)
xyz = list(zip_obj)
print(xyz)
"""


name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫香", "幸恵"]
longname = []
for n1, n2 in zip(name1, name2):
    longname.append(n1 + n2)
print(longname)

zip_obj = zip(name1, name2)
print(list(zip_obj))