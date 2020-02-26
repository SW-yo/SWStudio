#Datalogクラスが定義してあるモジュールをインポートする
from study_class_datalog import Datalog
#Datalogクラスを継承したMydataクラス
class Mydata(Datalog):
    def printlog(self):
        #スーパークラスのインスタンス変数の値を取り出す
        for date, data in self.loglist:
            print(date, data)

obj = Mydata()
obj.log("あいう")
obj.log("abc")
obj.log(123)
obj.printlog()
