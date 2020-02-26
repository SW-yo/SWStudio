class Simple:
    pass
Simple.x = 100
#print(Simple.x * 2)

def hello(msg = "ハロー"):
    print(msg)

Simple.greeting = hello
#Simple.greeting("おはよう！")
"""
obj = Simple()
obj.a = 123
print(obj.a)
"""
"""
obj1 = Simple()
obj2 = Simple()
def drum(beat = "トコトコ"):
    print(beat)
def sax(phrase = "ブーブー"):
    print(phrase)
obj1.play = drum
obj2.play = sax
obj1.play("ドンドコ")
obj1.play()
obj2.play()

obj1.a = None
obj1.play = None
del Simple.x
"""

class A:
    def hello(self):
        print("ハロー")
class B(A):
    def bye(self):
        print("グッバイ")

obj = B()
obj.hello()
obj.bye()
