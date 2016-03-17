
def predict():
	data = np.genfromtxt('./data/train.csv',delimiter = ',')
	print 'read data'
	X = preprocessing.scale(data[1:1000,1:])
	Y = data[1:1000,0]
	Y = Y.reshape(Y.shape[0],1)
	X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33,random_state = 42)
	classifier = svm.SVC()
	classifier.fit(X_train,Y_train)
	preds = classifier.predict(X_test)
	confusion_matrix = metrics.confusion_matrix(preds,Y_test)
	print 'built model'
	accuracy_score = metrics.accuracy_score(preds,Y_test)
	print 'accuracy_score',accuracy_score
	joblib.dump(classifier,'svm_model.pkl')







