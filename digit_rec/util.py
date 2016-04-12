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
from sklearn.ensemble import RandomForestClassifier
import argparse
import sklearn.neural_network as sknn
from sknn.mlp import Classifier , Layer


digit_size = 28
digit_column_size = digit_size**2
parser = argparse.ArgumentParser()
parser.add_argument("src")
parser.add_argument("--mode",help='simple or params',choices=['simple','params'])
parser.add_argument("--model",help='random forest or svm or ANN',choices=['rf','svm','ann'])
args = parser.parse_args()


