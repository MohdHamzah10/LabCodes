from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

pred = model.predict(X_test)

cm = confusion_matrix(y_test, pred)
acc = accuracy_score(y_test, pred)
pre = precision_score(y_test, pred, average='macro')
rec = recall_score(y_test, pred, average='macro')
f1 = f1_score(y_test, pred, average='macro')

print(cm)
print("Accuracy Score: ",acc)
print("Precision Score: ",pre)
print("Recall Score: ",rec)
print("F1 Score: ",f1)