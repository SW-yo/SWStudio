"""
import matplotlib.pyplot as plt
data = [2., 2.3, 4.1, 2.4, 5.3, 3.2, 4.6]
plt.plot(data)
plt.show()
"""
"""
import matplotlib.pyplot as plt
price = [200, 300, 400, 500, 600]
count = [31, 29, 25, 28, 26]
plt.plot(price, count, marker="o")
plt.xlabel("price")
plt.ylabel("count")
plt.grid(True)
plt.show()
"""
"""
import matplotlib.pyplot as plt
import math
X = range(0, 360)
S = [math.sin(math.radians(d)) for d in X]
C = [math.cos(math.radians(d)) for d in X]
plt.plot(X, S)
plt.plot(X, C)
#plt.savefig("sin.png")
plt.show()
"""
"""
import matplotlib.pyplot as plt
X = [100, 200, 300, 400, 500]
Y1 = [40, 65, 80, 100, 90]
Y2 = [34, 56, 75, 91, 79]
Y3 = [25, 47, 68, 76, 73]
Y4 = [15, 40, 52, 64, 69]
plt.plot(X, Y1, marker="o", color="blue", linestyle = "-", label="Y1")
plt.plot(X, Y2, marker="v", color="red", linestyle = "--", label="Y2")
plt.plot(X, Y3, marker="^", color="green", linestyle = "-.", label="Y3")
plt.plot(X, Y4, marker="d", color="m", linestyle = ":", label="Y4")
plt.legend(loc = "upper left")
plt.show()
"""
"""
import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
x_pos = range(0, 10)
V = [91, 45, 17, 88, 47, 87, 49, 56, 67, 77]
plt.bar(x_pos, V, tick_label=labels)
plt.show()
"""
"""
import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D", "E"]
y_pos = range(0, 5)
V = [91, 45, 17, 88, 47]
plt.barh(y_pos, V, tick_label=labels)
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100)
V = np.random.rand(100)*1000 + 50
plt.scatter(X, Y, s=V, c="b", alpha=0.3, linewidth=1, edgecolors="b")
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100)
V = np.random.rand(100)
plt.scatter(X, Y, s=200, c=V, cmap="Blues", edgecolors="b")
plt.colorbar()
plt.grid(True)
plt.show()
"""

import matplotlib.pyplot as plt
labels = ["E", "D", "C", "B", "A"]
V = [17, 25, 47, 68, 91]
ex = [0, 0, 0.1, 0 ,0]
plt.pie(V, explode=ex, labels=labels, autopct='%1.1f%%', startangle=90)
plt.show()
