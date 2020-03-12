while True:
    height = input('身長(cm)？：')
    if len(height) == 0:
        #Enterキーだけ押された場合は終了です
        break
    #入力は文字列なので小数に変換します
    height = float(height) / 100
    weight = input('体重(kg)：？')
    weight = float(weight)
    #組み込み関数powで累乗を計算できます
    bmi = weight / pow(height, 2)

    #小数点以下第１までの出力にフォーマットします
    print('BMI値は{:.1f}です。'.format(bmi))
    if bmi < 18.5:
        print('少しやせすぎです。')
    elif 18.5<= bmi < 25.0:
        print('標準的な体重です。')
    elif 25.0 <= bmi < 30.0:
        print('少し太っています。')
    else:
        print('高度の肥満です。')