from random import randint

"""
#5回のチケットで何ポイントもらえるか
tickets = 5
point = 0
fmt = "{:>3}"   #3桁右詰め
#ticketsが正の間は繰り返す
while tickets > 0:
    v = randint(1, 20)
    print(fmt.format(v))
    point += v
    tickets -= 1
#出力
print("-" * 3)
print(fmt.format(point))
"""

"""
#合計が21になる3つの値が出たらブレイク
while True:
    a = randint(1, 13)
    b = randint(1, 13)
    c = randint(1, 13)
    #合計が21ならブレイク
    if (a+b+c) ==21:
        break   #ブレイクする
print(a, b, c)
"""

"""
miss = 0    #間違えた回数
correct = 0 #正解数
print("問題！3回間違えたら終了。qで止める")
while miss < 3:
    a = randint(1, 100)
    b = randint(1, 100)
    ans =  a + b
    #問題を出題し、キーボードからの入力待ちにする
    question = f"{a}+{b}は？"
    value = input(question)
    #qと入力されたら中断する
    if value == "q":
        break   #ブレイクする
    #解答が正解かどうか判定する
    if value == str(ans):
        correct += 1
        print("正解です！")
    else:
        miss += 1
        print("間違い！", "×" * miss)   #間違いの回数を×で表示する
print("-" * 20)
print("正解：", correct)
print("間違い：", miss)
"""

"""
numbers = []    #からのリスト
#numbersの値が10個になるまで繰り返す
while len(numbers) < 10:
    n = randint(0, 100)
    if n in numbers:
        #nがnumbersに含まれていたらスキップする
        continue
    #numbersにnを追加する
    numbers.append(n)
print(numbers)
"""

numbers = []    #からのリスト
#numbersの値が10個になるまで繰り返す
while len(numbers) < 10:
    n = randint(-10, 90)
    if n<0:
        #nがマイナスならブレイクする
        print("中断されました")
        break
    if n in numbers:
        #nがnumbersに含まれていたらスキップする
        continue
    #numbersにnを追加する
    numbers.append(n)
else:
    print(numbers)
