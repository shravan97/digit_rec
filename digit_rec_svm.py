from sklearn.datasets import load_digits
from sklearn import svm,metrics
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn.grid_search import GridSearchCV
import numpy as np
import pickle
from sklearn.externals import joblib

digits = load_digits()
no_samples = len(digits.data)
X = digits.data
Y = digits.target
Y = Y.reshape(Y.shape[0],1)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33,random_state = 42)
scores_across_gammas = []


parameters = [{'kernel':['rbf'],'gamma':[1e-2,1e-3,1e-4]},
			 {'kernel':['linear'],'gamma':[1e-2,1e-3,1e-4],'degree':[1,2,3,4,5,6,7,8,9,10]}]

classifier = GridSearchCV(svm.SVC(),parameters)
classifier.fit(X_train,Y_train.reshape(Y_train.shape[0],))
cross_validation_scores = cross_val_score(classifier,X_train,Y_train.reshape(Y_train.shape[0],),cv = 5)
print cross_validation_scores
	
joblib.dump(classifier,'svm_model.pkl')







