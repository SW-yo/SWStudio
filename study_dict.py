"""
stock = {"S":7, "M":12, "L":3}
print(len(stock))
"""
"""
data = dict([("yellow", 3), ("blue", 6), ("green", 5)])
print(data)
"""
"""
keys = ["yellow", "blue", "green"]
values = [3, 6, 5]
data = dict(zip(keys, values))
print(data)
"""
"""
data = dict((["yellow", 3], ["blue", 6], ["green", 5]))
print(data)
"""
"""
data = dict(yellow = 3, blue = 6, green = 5)
print(data)
"""
"""
stock = dict.fromkeys(["S", "M", "L"], 0)
print(stock)
"""
"""
data = dict.fromkeys("abcd")
print(data)
"""
"""
data = dict(yellow = 3, blue = 6, green = 5)
data["blue"] = 10
data["white"] = 5
print(data)
"""
"""
data = dict(yellow = 3, blue = 6, green = 5)
data.setdefault("blue", 10)
data.setdefault("white", 10)
print(data)
"""
"""
d1 = {}
d2 = dict()
print(d1)
print(d2)
"""
"""
number = {}
number["one"] = 1
number["two"] = 2
number["three"] = 3
number["four"] = 4
print(number)
"""
"""
data = {"a":10, "b":20, "c":30}
newdata = {"a":15, "d":99}
data.update(newdata)
print(data)
print(newdata)
"""
"""
fruits = {"apple":7, "orange":5, "mango":3}
#del fruits["mango"]
fruits.clear()
print(fruits)
"""
"""
from random import randint
keys = ["green", "red", "blue", "yellow"]
data = {key: randint(1,100) for key in keys}
print(data)
"""
"""
unicode = {letter:ord(letter) for letter in "hello"}
print(unicode)
"""
"""
data = {"a":100, "b":200, "c":300}
#data_b = data
data_b = data.copy()
data_b["c"] = 0
print(data_b)
print(data)
"""
"""
import pprint
fruits = {"apple":7, "orange":5, "mango":3, "peach":6}
fruits2 = dict.fromkeys(fruits, 0)
pprint.pprint(fruits2)
"""
"""
members = {"東京":21, "大阪":16, "福岡":11}
print(members["東京"])
print(members["沖縄"])
"""
"""
city = input("調べる地区名：")
members = {"東京":21, "大阪":16, "福岡":11}
try:
    value = members[city]
    print(f"{city}の値は{value}です")
except KeyError:
    print(f"{city}のデータはありません")
except Exception as error:
    print(error)
"""
"""
members = {"東京":21, "大阪":16, "福岡":11}
#print(members.get("福岡"))
#print(members.get("京都"))
print("東京" in members)
"""
"""
fruits = {"apple":7, "orange":5, "mango":3, "peach":6}
for key in fruits:
    value = fruits[key]
    print(f"{key}が{value}個です")
"""
"""
fruits = {"apple":7, "orange":5, "mango":3, "peach":6}
#print(fruits.keys())
#keys = list(fruits.keys())
#print(keys)
#keys = [key.capitalize() for key in fruits.keys()]
#print(keys)
#print(fruits.values())
#values = list(fruits.values())
#print(values)
#print(sum(fruits.values()))
#print(fruits.items())
#print(list(fruits.items()))
for key, value in fruits.items():
    print(f"{key}が{value}個")
fruits.pop("apple")
print(fruits)
"""
"""
fruits = {"apple":7, "orange":5, "mango":3, "peach":6}
while fruits:
    key = input("どのフルーツを取り出しますか？（qで終了):")
    if key == "":
        continue
    elif key == "q":
        print("終了しました。")
        break
    try:
        value = fruits.pop(key)
        print(f"{key}は{value}個")
    except KeyError:
        print(f"{key}はありません。")
    except Exception as error:
        print(error)
        break
else:
    print("もう空っぽです。")
"""

fruits = {"apple":7, "orange":5, "mango":3, "peach":6}
#print(fruits.popitem())
#print(fruits)
while fruits:
    ans = input("フルーツを取り出しますか？(y/n):")
    if ans == "y":
        key, value = fruits.popitem()
        print(f"{key}は{value}個")
    elif ans =="n":
        print("終了しました。")
        break
else:
    print("もう空っぽです。")