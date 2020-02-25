"""
def do(func):
    func()
def thanks():
    print("ありがとう")
def hi():
    print("やあ！")
condition = 2
if condition == 1:
    do(thanks)
else:
    do(hi)
"""
"""
def calc(func, arg=1):
    price = func(arg)
    return price
def child(arg):
    return 400 * arg
def adult(arg):
    return 1200 * arg
#年齢によって計算する関数を変える
age = 12
num = 3
if age < 16:
    prince = calc(child, num)
else :
    price = calc(adult, num)
print(f"{age}歳、{num}人は{prince}円です。")
"""
"""
#クロージャの定義
def charge(price):
    #関数の実体
    def calc(num):
        return price * num
    return calc
#クロージャ（関数オブジェクト）を２種類
child = charge(400)
adult = charge(1000)
#料金を計算する
price1 = child(3)
price2 = adult(2)
print(price1)
print(price2)
"""
"""
#def area(w, h):
#    return w * h
#num = area(3, 4)
#print(num)
#func = lambda w, h : w * h
#num = func(3, 4)
#print(num)
#num = (lambda w, h: w * h)(3, 4)
price = lambda burger=1, potato=0 : burger*240 + potato*100
print(price(potato = 2))
"""
"""
def size(item):
    sizelist = ["XS", "S", "M", "L"]
    pos = sizelist.index(item)
    return pos
#並び替えるリスト
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key = size)
print(data)
"""
"""
sizelist = ["XS", "S", "M", "L"]
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key = lambda item : sizelist.index(item))
print(data)
"""
"""
def double(x):
    return x * 2
nums2 = list(map(double, nums))
nums = [4, 3, 7, 6, 2, 1]
print(nums2)
"""
"""
nums = [4, 3, 7, 6, 2, 1]
nums2 = list(map(lambda x : x * 2, nums))
print(nums2)
"""
"""
nums = [4, 3, 7, 6, 2, 1]
nums2 = [num * 2 for num in nums]
print(nums2)
"""
"""
nums = [4, -3, 9, 1, -2, -4, 5]
nums2 = list(filter(lambda x : x>0, nums))
print(nums2)
"""
"""
nums = [4, -3, 9, 1, -2, -4, 5]
nums2 = [num for num in nums if num>0]
print(nums2)
"""
"""
colors = ["red", "blue", "green", "yellow"]
colors_iter = iter(colors)
#print(type(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
"""
"""
def menu_generator():
    yield "ワイン"
    yield "サラダ"
    yield "スープ"
    yield "ステーキ"
    yield "アイスクリーム"
menu = menu_generator()
print(type(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
menu = menu_generator()
for item in menu :
    print(item)
"""
"""
#FizzBuzzジェネレータ
def fizzbuzz():
    n = 1
    while True:
        if n%15 == 0:
            yield "FizzBuzz"
        elif n%3 == 0:
            yield "Fizz"
        elif n%5 ==0:
            yield "Buzz"
        else:
            yield str(n)
        n += 1
#fizzbuzz()でジェネレータを作って20回呼び出す
game = fizzbuzz()
for i in range(0, 20):
    print(next(game))
"""
"""
def word_quiz(word):
    hint = ""
    for letter in word:
        hint += letter
        yield hint
#出題する
ans = "Python"
quiz = word_quiz(ans)
while True:
    try:
        hint = next(quiz)
        print(hint)
        word = input("この単語は？:")
        if ans.lower() == word.lower():
            point = len(ans) - len(hint)
            print(f"正解です！得点：{point}")
            break
        else:
            print("違います")
    except:
        print("終了です。得点：0")
        break
"""
"""
odd_gen = (odd for odd in range(1, 6, 2))
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
"""
"""
even_data = (even for even in range(0, 10, 2))
print(list(even_data))
"""
"""
def testgen():
    n = 0
    while True:
        received = yield n
        if received:
            n = received
        else:
            n = n + 1
gen = testgen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
gen.send(10)
print(next(gen))
print(next(gen))
print(next(gen))
"""

import study_advfunc_subgenerator
gen = study_advfunc_subgenerator.main_gen(3)
print(list(gen))
