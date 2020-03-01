"""
import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), [61, 45, 27, 88, 47]
X2, Y2 = range(0, 5), [17, 39, 46, 40, 27]
labels = ["A", "B", "C", "D", "E"]
fig = plt.figure()
#1行2列の左
ax1 = fig.add_subplot(1, 2, 1)
ax1.bar(X1, Y1, color="b", tick_label=labels)
ax1.set_title("dog")
#1行2列の右
ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(X2, Y2, color="g", tick_label=labels)
ax2.set_title("cat")
plt.show()
"""
"""
import matplotlib.pyplot as plt
X1, Y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
X2, Y2 = range(0, 7), [17, 39, 46, 40, 27, 35, 41]
labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()
#2行1列の左
ax1 = fig.add_subplot(2, 1, 1, facecolor="gray")
ax1.bar(X1, Y1, color="b", tick_label=labels)
ax1.set_title("snake")
#1行2列の右
ax2 = fig.add_subplot(2, 1, 2, facecolor="gray")
ax2.bar(X2, Y2, color="g", tick_label=labels)
ax2.set_title("fish")
plt.tight_layout()
plt.show()
"""
"""
import matplotlib.pyplot as plt
X1, Y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
X2, Y2 = range(0, 5), [77, 49, 56, 67, 76]
X3, Y3 = range(0, 4), [56, 41, 67, 76]
labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()
#2行1列の上
ax1 = fig.add_subplot(2, 1, 1)
ax1.bar(X1, Y1, color="b", tick_label=labels)
ax1.set_title("dog")
#2行2列の3番（下の左）
ax2 = fig.add_subplot(2, 2, 3)
ax2.bar(X2, Y2, color="g", tick_label=labels[:5])
ax2.set_title("cat")
#2行2列の4番（下の右）
ax3 = fig.add_subplot(2, 2, 4)
ax3.bar(X3, Y3, color="c", tick_label=labels[:4])
ax2.set_title("bird")
plt.tight_layout()
plt.show()
"""

import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), [61, 45, 27, 88, 47]
X2, Y2 = range(0, 5), [17, 39, 46, 40, 27]
labels = ["A", "B", "C", "D", "E"]
fig = plt.figure()
#Y軸を共有する2個のサブプロットを追加する
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)
#ax1 = fig.add_subplot(1, 2, 1)
ax1.bar(X1, Y1, color="b", tick_label=labels)
ax1.set_title("dog")
#ymin, ymax = plt.ylim()
#ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(X2, Y2, color="g", tick_label=labels)
ax2.set_title("cat")
#plt.ylim(ymin, ymax)
plt.show()
