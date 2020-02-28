# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:41:20 2020

@author: salt_
"""
"""
file = "./data/fox.txt"
#fileobj = open(file)
#text = fileobj.read()
#fileobj.close()
#print(text)
with open(file) as fileobj:
    text = fileobj.read()
    #print(text)
    newtext = text.rstrip(".")
    wordlist = newtext.split(" ")
    print(wordlist)
"""
"""
file = "./data/tsuretsuregusa.txt"
with open(file, "r", encoding="UTF_8") as fileobj:
    while True:
        line = fileobj.readline()
        aline = line.rstrip()
        if aline:
            print(aline)
        else:
            break
"""
"""
file = "./data/tsuretsuregusa.txt"
target = "心"
with open(file, "r", encoding="UTF_8") as fileobj:
    while True:
        try:
            line = next(fileobj)
            if line.find(target) >= 0:
                print(f"「{target}」が見つかりました")
                print(line, end = "")
                break
        except StopIteration:
            print(f"「{target}は見つかりませんでした")
            break
"""
"""
file = "./data/numdata.txt"
limit = 2.0
with open(file, "r", encoding="UTF_8") as fileobj:
    for i, line in enumerate(fileobj):
        if line == "\n":
            continue
        datalist = line.split(",")
        #limmit以下のとき1、大きいとき0に変換する
        result = [int(float(num)<=limit) for num in datalist]
        print(f"(i):{result}")
"""
"""
file = "smple.txt"
#fileobj = open(file, "w", encoding="UTF_8")
#fileobj.write("こんにちは\n")
#fileobj.write("Pythonをはじめよう\n")
#fileobj.close()
with open(file, "w", encoding="UTF_8") as fileobj:
    fileobj.write("こんにちは\n")
    fileobj.write("Pythonをはじめよう\n")
"""
"""
import sys
from datetime import datetime
file = "log.txt"
if len(sys.argv)<2:
    sys.exit()
now = str(datetime.now())
memo = sys.argv[1]
line = "-" * 10
with open(file, "a") as fileobj:
    fileobj.write(now + "\n")
    fileobj.write(memo + "\n")
    fileobj.write(line + "\n")
"""
"""
import tkinter as tk
import tkinter.filedialog as fd
from random import random
#書き出すデータを作る
def getdata():
    num = random()
    return str(num)
#tkアプリウィンドウを表示しない
root = tk.Tk()
root.withdraw()
#保存ダイアログを表示する
file = fd.asksaveasfilename(
    initialfile = "mydata",
    defaultextension = ".txt",
    title = "保存場所を選んでください",
    filetypes = [("TEXT", ".txt")]
)
#パスが選ばれたなら保存する
savedata = getdata()
if file:
    with open(file, "w", encoding="UTF_8") as fileobj:
        len = fileobj.write(savedata)
        print(f"{len}文字保存しました")
"""
"""
import os
print(os.path.exists("./data"))
print(os.path.exists("./data2"))
"""

import os
from random import randint
#保存フォルダとファイルパス
folder = "./data/"
file = folder + "sample.txt"
#ファイルを保存する
def filewrite():
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file, "w", encoding="UTF_8") as fileobj:
        num = randint(0, 100)
        fileobj.write(f"{num}が出ました")
        print("ファイルを保存しました")
#既存のファイルの有無チェック
if os.path.exists(file):
    while True:
        answer = input("上書きしても良いですか？(y/n))")
        if answer == "y":
            filewrite()
            break
        else:
            break
else:
    filewrite()
