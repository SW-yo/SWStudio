#formaqtの練習

from random import randint

num = randint(0,100)

if num <= 50:
    result = "このばかちんが"
else:
    result = "がんばったな"

text = f"{num}点だなんて{result}"
print(text)
