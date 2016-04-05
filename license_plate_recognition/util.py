from sklearn.datasets import load_digits
from sklearn import svm,metrics,preprocessing
from sklearn.cross_validation import train_test_split,cross_val_score
from sklearn.grid_search import GridSearchCV
import numpy as np
import pickle
from sklearn.externals import joblib
import sys
import cv2
import scipy


digit_size = 28
digit_column_size = digit_size**2
src = None	

