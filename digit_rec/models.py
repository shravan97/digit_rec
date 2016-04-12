from util import *
import util

def model(model_type):
	classifier = None
	if( model_type == 'svm' ):
		classifier = svm.SVC()
	elif( model_type == 'rf'):
		classifier = RandomForestClassifier()
	elif( model_type == 'ann' ):
		classifier = Classifier(layers=[Layer("Softmax" , units=1000),Layer("Softmax" , units=10)],learning_rate=0.02,n_iter=1000)
	return classifier


