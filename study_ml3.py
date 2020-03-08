from sklearn import datasets
from sklearn import linear_model
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

boston = datasets.load_boston()
#print(boston.DESCR)

boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df["Price"] = boston.target
#print(boston_df[:5])

rooms_train = DataFrame(boston_df["RM"])
y_train = boston.target
model = linear_model.LinearRegression()
model.fit(rooms_train, y_train)

rooms_test = DataFrame(np.arange(rooms_train.values.min(), rooms_train.values.max(), 0.1))
prices_test = model.predict(rooms_test)

plt.scatter(rooms_train.values.ravel(), y_train, c="b", alpha=0.5)
plt.plot(rooms_test.values.ravel(), prices_test, c ="r")
plt.title("Boston House Prices dataset")
plt.xlabel("rooms")
plt.ylabel("price $1000's")
plt.show()
