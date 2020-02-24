# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:38:09 2020

@author: saito yoichiro
"""

"""
def price(adult, child):
    return ((adult * 1200) + (child * 500))

#print(price(1, 2))
print(price(adult = 1, child = 2))
print(price(child = 2, adult = 1))
"""
"""
#def calc(size, num = 6):
def calc(size = "M", num = 6):
    unit_price = {"S" : 120, "M" : 150, "L" : 180}
    price = unit_price[size] * num
    return (size, num, price)
#calcを試す
a = calc("S", 2)
#print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")
b = calc("M")
#print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")
c = calc()
print(f"{c[0]}サイズ、{c[1]}個、{c[2]}円")
d = calc("L")
print(f"{d[0]}サイズ、{d[1]}個、{d[2]}円")
e = calc(num = 1)
print(f"{e[0]}サイズ、{e[1]}個、{e[2]}円")
"""
"""
def fruit(*args):
    print(args)
fruit()
fruit("リンゴ", "みかん", "いちご", "バナナ")
"""
"""
def route(start, end, *args):
    #引数からルートのリストを作る
    route_list = [start]
    route_list += list(args)
    route_list += [end]
    #リストの要素を矢印で連結した文字列にする
    route_str = "→".join(route_list)
    print(route_str)
#route()を試す
start = "東京"
end = "宮崎"
route(start, end, "神戸", "長崎", "熊本")
"""
"""
def fruit(**kwargs):
    print(kwargs)
fruit(apple=2, orange=3, banana=1)
"""

def entry(name, gender, **kwargs):
    data = {"name" : name, "gendr" : gender}
    data.update(kwargs)
    print(data)
#entry()を試す
entry(name="大山坂道", gender="男性", age=27, course="E")
