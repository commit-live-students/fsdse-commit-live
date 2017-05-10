from unittest import TestCase
import pickle
from sklearn.metrics import accuracy_score


class TestBuild_model(TestCase):
    def test_accuracy(self):
        try:
            from build_model import build
        except ImportError:
            self.assertFalse("No build method found. Please initialize build method and return ML model.")

        try:
            X_test, y_test = pickle.load(open("data/german_test.p", "rb"))
        except:
            self.assertFalse(
                "No test file. Either you have moved location and deleted the file. Very soon we are changing this approach so that test cases and test data will not be part of repo so that Student can not change / delete it.")

        creditClf = build()
        y_pred = creditClf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Your accuracy is " + str(accuracy))
        self.assertGreater(accuracy, 0.78, "Accuracy not acceptable. You can do better with other approach.")