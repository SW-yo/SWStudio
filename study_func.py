"""
def hello():
    return "Hello!!"

msg = hello()
print(msg)
"""
"""
from random import randint

#関数を定義する
def dice():
    num = randint(1,6)
    return num

#dice()を呼び出す
for i in range(5):
    result = dice()
    print(result)

#２個のサイコロを５回降った結果
for i in range(5):
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    print(f"{dice1}と{dice2}で合計{sum}")
"""
"""
def mile2meter(mile):
    meter = mile * 1609.344
    return meter
#20マイルをメートルに換算する
distance = mile2meter(20)
print(distance)
"""
"""
#三角形の面積
def triangle(base, height):
    area = base * height / 2
    return area
#関数を試す
b = 15
h = 13
v = triangle(h, b)
print(f"底辺{b}、高さ{h}の三角形の面積は{v:.1f}です。")
"""
"""
from random import randint
#サイコロを定義する
def dice():
    num = randint(1,6)
    return num
#2個のサイコロを振るゲーム
def dicegame():
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    if sum % 2 == 0:
        print(f"{dice1}と{dice2}で合計{sum}、偶数")
    else:
        print(f"{dice1}と{dice2}で合計{sum}、奇数")
#dicegame()を5回行う
for i in range(5):
    dicegame()
print("ゲーム終了")
"""
"""
def calc(num):
    unit_price = 180
    if not num.isdigit():
        return None
    price = int(num) * unit_price
    return price
#キーボードから引数を入力して試す
while True:
    num = input("個数を入れてください。（qで終了）:") 
    if num == "":
        continue
    elif num == "q":
        break
    #calcで計算する
    result = calc(num)
    print(result)
"""
"""
def calc(num):
    unit_price = 180
    try:
        num = float(num)
        return num * unit_price
    except:
        return None
#キーボードから引数を入力して試す
while True:
    num = input("個数を入れてください。（qで終了）:") 
    if num == "":
        continue
    elif num == "q":
        break
    #calcで計算する
    result = calc(num)
    print(result)
"""

v = 2
def calc():
#    v = 2
#    v = v * 10
#    ans = 3 * v
    v_local = v * 10
    ans = 3 * v_local
    print(ans)
calc()
print(v)