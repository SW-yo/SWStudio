"""
while True:
    num = input("何個ですか？(qで終了）")
    if num == "q":
        print("終了しました")
        break
    #入力された値を整数にできない場合例外処理を行う
    try:
        price = 120 * int(num)
        print("金額",price)
    except:
        print("エラーです。正しい数値を入力してください")
"""

"""
num = 0
try:
    value = 120 / num
    print(value)
except :
    print("エラーになりました")
finally:
    print("計算終了")
"""

"""
sum = 7600
while True:
    num = input("何人ですか？（qで終了）")
    if num == "q":
        print("終了しました")
        break
    #例外を振り分けて例外処理を行う
    try:
        price = round(sum / int(num))
        if price < 0:
            #マイナスの場合は無視
            continue
        print("一人あたりの金額：", price)
    except ValueError:
        print("数値を入れてください")
    except ZeroDivisionError:
        print("0以外の数値を入力してください")
"""

sum = 7600
while True:
    num = input("何人ですか？（ｑで終了）")
    if num == "q":
        print("終了しました")
        break
    #例外を処理する
    try:
        price = round(sum / int(num))
    except Exception as error:
        print("エラーになりました")
        print(error)
    else:
        if price < 0:
            #マイナスの場合は無視
            continue
        print("一人あたりの金額：", price)
