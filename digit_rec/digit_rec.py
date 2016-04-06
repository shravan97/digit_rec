from util import *
import util
import ingestor
import models

def initialization():
	'''
		Method with parameters to allow user to change datasize and models.
		To be renamed as one initialization
		Ingest
		Preprocess
		Fit Model 
		Make Predictions 
		Persist the Model 
	'''	
	src = './data/train.csv'
	this_model = args.model
	data = ingestor.ingest(src)
	print 'read data'
	X_train, X_test, Y_train, Y_test = ingestor.preprocess(data)
	print 'preprocessed data'
	classifier = models.model(this_model)
	classifier.fit(X_train,Y_train.reshape(Y_train.shape[0],))
	print 'built model'
	preds = classifier.predict(X_test)
	print 'made predictions'
	accuracy_score = metrics.accuracy_score(preds,Y_test.reshape(Y_test.shape[0],))
	print 'accuracy score is',accuracy_score
	joblib.dump(classifier,this_model+'.pkl')



def predict_digit_image(classifier):
	'''
		Default Method, Reads an input image of any size and outputs a digit.
	'''	

	img = cv2.imread(args.src)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img = scipy.misc.imresize(img,(util.digit_size,util.digit_size))
	img = img.flatten().reshape(1,util.digit_column_size)
	prediction = classifier.predict(img)[0]
	print 'prediction is', prediction
	return prediction



def predict(src=None):
	classifier = None
	if( args.mode == 'simple' ):
		args.model = 'svm'
	try:
		classifier = joblib.load('./'+args.model+'_model.pkl')
	except IOError:
		print 'Initializing to be done, please wait'
		initialization()
		classifier = joblib.load('./'+args.model+'_model.pkl')
	return predict_digit_image(classifier)



	







