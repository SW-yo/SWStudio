"""
print(range(-5, 6))
thelist = list(range(-5, 6))
print(thelist)
"""

"""
colors = ["blue", "red", "green", "yellow"]
colors[2] = "black"
print(colors)
"""

"""
list = [[["p", "y"], ["t", "n"]], [["o", "n"], ["3", "note"]]]
print(list[0])
print(list[0][0])
print(list[0][0][0])
"""

"""
r101 = "佐藤"
r102 = "田中"
r103 = "鈴木"
r201 = "青木"
r202 = "廣田"
r203 = "野村"
floor1 = [r101, r102, r103]
floor2 = [r201, r202, r203]
apartment = [floor1, floor2]
print(apartment[0][1])
r102 = "マイケル"
print(apartment[0][1])
apartment[0][1] = "マイケル"
print(apartment[0][1])
"""

"""
pos = int(input("取り出す位置：")) #リストから取り出す位置を入力する
colors = ["blue", "red", "green", "yellow"]
length = len(colors) #リストの長さ(要素の個数)
if -length <= pos < length:
     item = colors[pos]
     print(item)
else:
    print("エラーになりました。")
"""

"""
pos = int(input("取り出す位置：")) #リストから取り出す位置を入力する
colors = ["blue", "red", "green", "yellow"]
#例外処理を組み込む
try:
    item = colors[pos]
    print(item)
except IndexError:
    print("インデックスエラーです")
except Exception as error:
    print(error)
"""

"""
data = []
data.append(10)
data.append(20)
print(data)
data.append(30)
print(data)
data.insert(2, 40)
print(data)
"""

"""
#fruits = ["aple", "orange", "banana", "peach"]
fruits = []
#dessert = fruits.pop()
dessert = fruits.pop(0)
print(dessert)
print(fruits)
"""

"""
#fruits = ["aple", "orange", "banana", "peach"]
fruits = []
#fruitsがから出ないかチェックする
if fruits:
    dessert = fruits.pop()
    print("デザートは" + dessert)
print(fruits)
"""

"""
fruits = []
#例外処理に組み込む
try:
    dessert = fruits.pop()
    print("デザートは" + dessert)
    print(fruits)
except:
    print("エラーになりました。")
"""

"""
colors =  ["blue", "red", "green", "red",  "yellow"]
print("削除前", colors)
target = "green"
#削除する値が含まれているならば削除する
if target in colors:
    colors.remove(target)
print("削除後", colors)
"""

"""
colors =  ["blue", "red", "green", "red",  "yellow"]
print("削除前", colors)
target = "red"
#削除する値が含まれている間は削除する
while target in colors:
    colors.remove(target)
print("削除後", colors)
"""

"""
message = "may the force be with you"
words = message.split()
print(words)
"""

"""
fruits = "apple, orange, banana, mango"
fruits_list = fruits.split(", ")
print(fruits_list)
"""

"""
colors = "red, blue,  green, white , black"
colors = colors.replace(" ", "") #空白を取り除く
color_list = colors.split(",") #カンマで分割する
print(color_list)
"""

"""
result = "23, 45, 56, 87, 90, 123, 231, 256, 321"
#result_list = result.split(",", 3)
#print(result_list)
top3 = result.split(",", 3)[:3]
print(top3)
"""


members = ["Tom", "Jerry", "Spike"]
name = " and ".join(members)
print(name)
