from util import *
import util
def model(model_type):
	classifier = None
	if( model_type == 'svm' ):
		classifier = svm.SVC()
	elif( model_type == 'rf'):
		classifier = RandomForestClassifier()
	elif( model_type == 'ann' ):
		classifier = None
	return classifier


