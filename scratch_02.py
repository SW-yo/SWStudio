from matplotlib import pyplot as plt
from collections import Counter

"""
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#折線グラフを作る。X軸を年、Y軸をGDPとする。
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#タイトルに追加する
plt.title("Nominal GDP")

#Y軸にラベルを追加する
plt.ylabel("Billions $")
plt.show()
"""
"""
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#X軸の幅のデフォルトは0.8なので、左側に0.1を加えてセンタリングさせる
xs = [i + 0.1 for i, _ in enumerate(movies)]

#軸を[xs]、高さを[num_oscars]で棒グラフを作る
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Faborite Movies")

#X軸のラベルに映画名を棒の中心に配置する
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()
"""
"""
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade : grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],  #グラフの棒を左に4ずらす
        histogram.values(),                 #値に合わせた硬さ設定
        8)                                  #棒の幅を8にする

plt.axis([-5, 105, 0, 5])                   #X軸の範囲を-5から105とする
                                            #Y軸の範囲を0から5とする

plt.xticks([10 * i for i in range(11)])     #X軸のラベル0,10,…,100を設定
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
"""
"""
mentions = [500, 505]
years = [2013, 2014]

plt.bar(years, mentions, align="center")
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

#次の行を省略すると、0,1と共に+2.013e3がX軸上に
#表示されてしまう（matplotlibの欠点である）
plt.ticklabel_format(useOffset=False)

#Y軸の500以上の部分だけを表示すると、誤った印象を与える
#plt.axis([2012.5, 2014.5, 499, 506])
plt.axis([2012.5, 2014.5, 0, 550])
#plt.title("Look at the 'Huge' Increase!")
plt.title("Not So Huge Anymore")
plt.show()
"""
"""
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#plt.plotを複数回呼び出して1つのグラフに複数の線を描画可能
plt.plot(xs, variance, 'g-', label='variance')      #緑の実践
plt.plot(xs, bias_squared, 'r-.', label='bias^2')   #赤の点線
plt.plot(xs, total_error, 'b:', label='total error')#青の点線

#各線にラベルを指定しているので、凡例が自動で描かれる
#loc=9は「上部中央」を示す
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
"""
"""
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)

#各点のラベル
for label, friend_count, minutes_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minutes_count),   #各点にラベルを付加する
        xytext = (5, -5),                   #ただし、Ⅰは少し横にずらす
        textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.show()
"""

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel("test 1 grades")
plt.ylabel("test 2 grades")
plt.axis("equal")
plt.show()
