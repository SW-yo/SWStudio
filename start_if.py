import datetime
today = datetime.datetime.now()
print(today)

if today.weekday() < 4:
    print("力まず行こう")
elif today.weekday() == 4:
    print("ゆっくりやるよ")
else:
    print("だらっとしよう")