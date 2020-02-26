#Carクラス
class Car:
    #クラス変数
    maker = "peace"
    count = 0
    #クラスメソッド
    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数：{cls.count}")
    #初期化メソッド
    def __init__(self, color ="white"):
        Car.countup()
        self.mynumbewr = Car.count
        self.color = color
        self.mileage = 0
    #インスタンスメソッド
    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)
