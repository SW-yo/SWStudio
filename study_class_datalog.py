#datetimeモジュール
from datetime import datetime
#Datalogクラス
class Datalog:
    #初期化メソッド
    def __init__(self):
        self.loglist = []
    #インスタンスメソッド
    def log(self, data):
        now = datetime.now()
        item = (now, data)
        self.loglist.append(item)
