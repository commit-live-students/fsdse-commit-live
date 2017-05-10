#Importing necessary packages in Python
import pickle
import os

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
X_train, y_train = pickle.load(open(ROOT_DIR + "/data/german_train.p", "rb"))

def buildRandomForestClassifier():
    creditClf = RandomForestClassifier(n_estimators=20, random_state=1)
    creditClf.fit(X=X_train, y=y_train)
    return creditClf

def buildLogisticRegression():
    creditClf = LogisticRegression(random_state=1)
    creditClf.fit(X=X_train, y=y_train)
    return creditClf

build = buildRandomForestClassifier