from sklearn import svm
import joblib

#train classifier
X = [[0, 0], [0, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
#trained classifier as joblib file
joblib.dump(clf, "binary_clf.joblib")