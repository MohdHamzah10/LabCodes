from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)

m1 = LogisticRegression(max_iter=200)
m2 = DecisionTreeClassifier()
m3 = KNeighborsClassifier()

m1.fit(X_train, y_train)
m2.fit(X_train, y_train)
m3.fit(X_train, y_train)

print(m1.score(X_test, y_test))
print(m2.score(X_test, y_test))
print(m3.score(X_test, y_test))