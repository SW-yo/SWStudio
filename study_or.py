#randomモジュールのrandint関数を読み込む
from random import randint
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
