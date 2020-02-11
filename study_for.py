"""
#4行3列の点の座標を求める
for i in range(4): #4行
      print() #各行の改行
      for j in range(3): #3行
          x = j * 2
          y = i * 3
          print(f"({x}, {y})", end ="")
print() #最後の行の改行
"""

"""
numlist = [3, 4.2, 10, "x", 1, 9]
sum = 0
for num in numlist:
    #numが数値でないときはブレイクする
    if not isinstance(num, (int, float)):
        print(num, "数値ではありません")
        break #ブレイクする
    sum += num
    print(num, "/", sum)
"""

"""
for i in range(4):
    for j in range(4):
        if i < j :
            print("." * j)
            break
        print(f"i={i}, j={j}")
"""

"""
numlist = [3, 4.2, 10, "x", 1, 9]
sum = 0
for num in numlist:
    #numが数値でないときはブレイクする
    if not isinstance(num, (int, float)):
        print(num, "数値ではありません")
        continue #スキップする
    sum += num
    print(num, "/", sum)
"""

"""
for i in range(4):
    for j in range(4):
        if i < j :
            print("." * j)
            continue
        print(f"i={i}, j={j}")
"""


#numlist = [3, 4.2, 10, "x", 1, 9]
numlist = [3, 4.2, 10, 1, 9]
sum = 0
for num in numlist:
    #numが数値でないときはブレイクする
    if not isinstance(num, (int, float)):
        print(num, "数値ではありません")
        break #ブレイクする
    sum += num
else:
    #breakされなかったときは合計した値を出力する
    print("合計", sum)
