from util import *
import util


def predict_with_parms():
	'''
		Method with parameters to allow user to change datasize and models.
	'''	
	data = np.genfromtxt('./data/train.csv',delimiter = ',')
	print 'read data'
	X = preprocessing.scale(data[:,1:])
	Y = data[:,0]
	Y = Y.reshape(Y.shape[0],1)
	X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33,random_state = 42)
	classifier = svm.SVC()
	classifier.fit(X_train,Y_train.reshape(Y_train.shape[0],))
	preds = classifier.predict(X_test)
	print 'built model'
	accuracy_score = metrics.accuracy_score(preds,Y_test.reshape(Y_test.shape[0],))
	print 'accuracy_score',accuracy_score
	joblib.dump(classifier,'svm_model.pkl')

def predict_simple(src=None):
	'''
		Default Method, Reads an input image of any size and outputs a digit.
	'''

	if( src!= None ):
		img_src = src
	else:
		img_src = sys.argv[1]		
	classifier = joblib.load('./svm_model.pkl')
	img = cv2.imread(img_src)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	img = scipy.misc.imresize(img,(util.digit_size,util.digit_size))
	img = img.flatten().reshape(1,util.digit_column_size)
	prediction = classifier.predict(img)
	print 'prediction is', prediction[0]
	return prediction[0]



def predict(src=None):
	if(sys.argv[0] == '/usr/bin/nosetests'):
		return predict_simple(src)
	elif(len(sys.argv) < 3 ):
		return predict_simple()
	else:
		return predict_with_parms()


	







