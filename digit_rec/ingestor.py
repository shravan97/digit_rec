from util import *
import util

def ingest(src):
	'''
	READ DATA FROM FILE, RETURN NUMPY ARRAY
	'''
	data = np.genfromtxt(src,delimiter=',')
	return data

def preprocess(data):
	X = preprocessing.scale(data[:,1:])
	Y = data[:,0]
	Y = Y.reshape(Y.shape[0],1)
	X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33,random_state = 42)
	return X_train, X_test, Y_train, Y_test