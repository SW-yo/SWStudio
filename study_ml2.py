from sklearn import datasets
from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import ShuffleSplit
import matplotlib.pyplot as plt

iris = datasets.load_iris()
#print(iris.DESCR)

X = iris.data
y = iris.target

#print(X.shape)
#print(y.shape)
#print(X)
#print(iris.feature_names)
#print(y)

#setosa:0~49,versicoloe:50~99,virginica:100~149
"""
plt.scatter(X[:50, 0], X[:50, 1], color="r", marker="o", label="setosa")
plt.scatter(X[50:100, 0], X[50:100, 1], color="g", marker="+", label="versicoloe")
plt.scatter(X[100:, 0], X[100:, 1], color="b", marker="x", label="virginica")
"""
"""
for i, cl, mk, lb, in zip([0, 1, 2], "rgb", "o+x", iris.target_names):
    plt.scatter(X[y==i][:, 0], X[y==i][:, 1], color=cl, marker=mk, label=lb)
"""
"""
plt.title("Iris Plants Database")
plt.xlabel("speal length(cm)")
plt.ylabel("speal width(cm)")
plt.legend()
plt.show()
"""
"""
n_train = len(X)//2
X_train, X_test = X[:n_train], X[n_train:]
y_train, y_test = y[:n_train], y[n_train:]
clf = svm.SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
"""

ss = ShuffleSplit(train_size=0.6, test_size=0.4, random_state=0)
train_index, test_index = next(ss.split(X))
X_train, y_train = X[train_index], y[train_index]
X_test, y_test = X[test_index], y[test_index]

clf = svm.SVC()
#clf = linear_model.LogisticRegression()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
