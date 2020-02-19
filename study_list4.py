"""
names = ["鈴木", "田中", "栗林", "山岡"]
for who in names:
    print(who + "さん")
"""

"""
numbers = [2, 6, -3, 5, -1, 7]
sum = 0
#numbersの正の値だけを合算する
for num in numbers:
    if num > 0:
        sum += num
print(sum)
"""

"""
names = ["鈴木", "田中", "栗林", "山岡"]
for i, who in enumerate(names, 1):
    print(f"{i} : {who}さん")
"""

"""
name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
longname = []
#name1とname2を連結したリストを作る
for n1, n2 in zip(name1, name2):
    longname.append(n1 + n2)
print(longname)
"""

"""
nums = [1, 2, 3, 4, 5]
nums_double = [num*2 for num in nums]
print(nums_double)
"""

"""
import math
num_List = [5.1, 4.3, 8.2, 6.3, 9.6, 10.2, 2.3]
result = [math.floor(num) for num in num_List]
print(result)
"""

"""
numbers = [num for num in range(1, 10)]
print(numbers)
"""

"""
group_list = [str+"組" for str in "ABCDEFG"]
print(group_list)
"""

"""
name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
longname = [n1+n2 for n1, n2 in zip(name1, name2)]
print(longname)
"""

"""
numbers = [2.1, 0.2, 0.3, 1.4, 3.1, 0.3, 1.6]
result = [num for num in numbers if 1<=num<=2]
print(result)
"""

"""
numbers =[2.1, 4, "", 2.2, "1", 3]
numbers = [num for num in numbers if isinstance(num, (int, float))]
print(numbers)
"""

"""
numbers = [4, 12, 21, 32, 8, 6, 11, 16]
result = [num for num in numbers if num>=5 if num%2==0]
print(result)
"""

"""
data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = [num*2 for alist in data for num in alist]
print(result)
"""

"""
data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = [[num*2 for num in alist] for alist in data]
print(result)
"""

"""
colors = ["blue", "red", "green", "yellow"]
#print("green" in colors)
#print("black" in colors)
print("gree" in colors)
print("gre*" in colors)
"""

"""
names = ["鈴木裕子", "田中里美", "桜木颯太"]
name = "里美"
result = False
for item in names:
    if name in item:
        result = True
        break
print(result)
"""


"""
id_list = ["a2345", "a1236", "b7656", "f0987"]
#print(id_list.index("a1236"))
while True:
    id = input("idを入力してください（qで終了)：")
    if id == "q":
        print("終了しました")
        break
    #例外処理を組み込んで検索する
    try:
        pos = id_list.index(id)
        print(str(pos+1) + "番目のメンバーです")
    except:
        print("メンバーではありません")
"""

"""
numbers = [1, 3, 4, 5, 5, 15, 12, 57]
print(numbers.count(2))
print(numbers.count(4))
print(numbers.count(5))
"""

"""
letters = ["a", "ax", "b", "b", "bx"]
print(letters.count("a"))
print(letters.count("b"))
print(letters.count("c"))
"""

"""
result = [1, 1, 0, 0, 1, 0, 1, 1]
half = len(result) / 2
point = result.count(1)
if point >= half:
    print("合格")
else:
    print("不合格")
"""

"""
import random
fruits = ["apple", "orange", "banana", "peach"]
desert = random.choice(fruits)
print(desert)
"""

"""
import secrets
fruits = ["apple", "orange", "banana", "peach"]
desert = secrets.choice(fruits)
print(desert)
"""

"""
data = [56, 45, 83, 67, 59, 41, 77]
print(sum(data))
print(max(data))
print(min(data))
"""


judge = [8.7, 8.8, 9.0, 9.1, 8.5]
result = sum(judge) - max(judge) - min(judge)
print(result)