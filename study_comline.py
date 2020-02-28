"""
import sys
arglist = sys.argv
print(arglist)
"""
"""
import sys
if len(sys.argv) < 2:
    print("読み込むファイル名を指定してください")
    sys.exit()
file = sys.argv[1]
with open(file) as fileobj:
    text = fileobj.read()
    print(text)
"""

import tkinter as tk
import tkinter.filedialog as fd
#tkアプリウィンドウを表示しない
root = tk.Tk()
root.withdraw()
#オープンダイアログを表示する
file = fd.askopenfilename(
    title ="ファイルを選んでください",
    filetype=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)
#ファイルが選択されたならば開く
if file:
    with open(file, "r", encoding="utf_8") as fileobj:
        text = fileobj.read()
        print(text)
