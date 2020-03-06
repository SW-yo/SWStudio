from sklearn import datasets
digits = datasets.load_digits()
#print(digits.DESCR)
#print(digits.data.shape)
#print(digits.target.shape)
#print(digits.data)
#print(digits.target)
#print(digits.data[0])
#print(digits.images[0])

import matplotlib.pyplot as plt
"""
plt.matshow(digits.images[7], cmap="Greys")
plt.show()
print(digits.target[7])
"""

n_train = len(digits.data) * 2//3
X_train = digits.data[:n_train]
y_tarin = digits.target[:n_train]
X_test = digits.data[n_train:]
y_test = digits.target[n_train:]
#print([d.shape for d in [X_train, y_tarin, X_test, y_test]])

from sklearn import svm
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_tarin)
print(clf.score(X_train, y_tarin))

predicted = clf.predict(X_test)
print((y_test != predicted).sum())

from sklearn import metrics
#print(metrics.classification_report(y_test, predicted))
print(metrics.confusion_matrix(y_test, predicted))

imgs_yt_preds = list(zip(digits.images[n_train:], y_test, predicted))
for index, (image, y_t, pred) in enumerate(imgs_yt_preds[404:416]):
    plt.subplot(3, 4, index + 1)
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")
    plt.title(f"{y_t} pre:{pred}", fontsize=12)
plt.show()

print(clf)
