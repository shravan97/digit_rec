from sklearn.datasets import load_digits
from sklearn import svm,metrics,preprocessing
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn.grid_search import GridSearchCV
import numpy as np
import pickle
from sklearn.externals import joblib



data = np.genfromtxt('./data/train.csv',delimiter = ',')
print 'read data'
X = preprocessing.scale(data[:,1:])
Y = data[:,0]
Y = Y.reshape(Y.shape[0],1)



X,a,Y,b = train_test_split(X,Y,test_size = 0.9,random_state = 42)
print X.shape,Y.shape
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33,random_state = 42)
classifier = svm.SVC()
classifier.fit(X_train,Y_train)
preds = classifier.predict(X_test)
confusion_matrix = metrics.confusion_matrix(preds,Y_test)
print 'built model'
accuracy_score = metrics.accuracy_score(preds,Y_test)
print 'accuracy_score',accuracy_score

	
joblib.dump(classifier,'svm_model.pkl')







