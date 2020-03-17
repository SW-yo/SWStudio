import dice

num = input('4,6,8,12,20のどれで勝負しますか？：')
num = int(num)
my_dice = dice.Dice(num)
cpu_dice = dice.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = cpu_dice.shoot()

print('CPU: {}/あなた {}'.format(cpu_pip, my_pip))

if my_pip > cpu_pip:
    print('おめでとうございます。あなたの勝ちです！')
elif my_pip < cpu_pip:
    print('残念！あなたの負けです…')
else:
    print('引き分けです。')