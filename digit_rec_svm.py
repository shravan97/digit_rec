from sklearn.datasets import load_digits
from sklearn import svm,metrics
from sklearn.cross_validation import train_test_split,cross_val_score
import numpy as np

digits = load_digits()
no_samples = len(digits.data)
X = digits.data
Y = digits.target
Y = Y.reshape(Y.shape[0],1)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33,random_state = 42)
scores_across_gammas = []

#expected = Y_test
#predicted = classifier.predict(X_test)

#Use expected and predicted for final test only. Evaluate Model accuracy, parameter accuracy with cross validation score.

gamma_values = np.linspace(0.001,1,100)
for gamma_value in gamma_values:
	classifier = svm.SVC(gamma=gamma_value,kernel = 'rbf')
	classifier.fit(X_train,Y_train)
	cross_validation_scores = cross_val_score(classifier,X_train,Y_train.reshape(Y_train.shape[0],),cv = 5)
	mean_cross_validation_score = np.mean(cross_validation_scores)
	scores_across_gammas.append(mean_cross_validation_score)
	print gamma_value,mean_cross_validation_score

scores_across_gammas = np.array(scores_across_gammas)
print scores_across_gammas.shape




