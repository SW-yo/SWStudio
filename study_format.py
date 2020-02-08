#formaqtの練習

from random import randint

num = randint(0,100)

if num <= 50:
    result = "このばかちんが"
else:
    result = "がんばったな"

#text = f"また{num}点だなんて{result}！"
text = "{}点って{}！".format(num, result)
print(text)
