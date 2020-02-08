#randomモジュールのrandint関数を読み込む
from random import randint

"""
#or
size = randint(5, 20)   #5～20の乱数
weight = randint(20, 40)   #20～40の乱数
#判定（どちらか片方でもTrueならば合格）
if (size >= 10) or (weight >= 25):
    result = "合格"
else:
    result = "不合格"

#結果の出力ght}
text = f"サイズ{size}、重量{weight}:{result}"
print(text)
"""

"""
#not
name = ""
if not name:
    name = "匿名"
print(name)
"""

"""
from random import randint
num = randint(0, 100)
#奇数か偶数か判定する
if num % 2 :
    result = "奇数"
else:
    result = "偶数"
print(num, result)
"""

"""
a = randint(0, 10)  #0～10の乱数
#判定
if 5 <= a <=8:
    print(a, "合格")
else:
    print(a, "不合格")
"""

"""
a = randint(0, 100) #0～100の乱数
b = randint(0, 100)
#大きな方の値を代入する
if a > b:
    bigger = a
else:
    bigger = b
#結果の出力
text = f"{a}と{b}では{bigger}が大きい"
print(text)
"""

"""
a = randint(0, 100) #0～100の乱数
b = randint(0, 100)
#大きな方の値を代入する
bigger = a if a>b else b
#結果の出力
text = f"{a}と{b}では{bigger}が大きい"
print(text)
"""
