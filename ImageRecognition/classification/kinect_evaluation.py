from test_kinect_data_processing import get_data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import ensemble
from sklearn.externals import joblib
import os

folder = os.path.normpath(os.getcwd() + os.sep + os.pardir)
dir = os.path.normpath(folder + '/Datasets/kinect_training.csv')
data, labels = get_data(data_dir=dir)

def kfold(name, clf):
    print("\n" + name)
    avg_train = 0
    avg_test = 0
    fold_number = 0

    #Do K-Fold cross validation on the data
    from sklearn.model_selection import KFold
    kf = KFold(n_splits=10, shuffle=True)
    for train_indices, test_indices in kf.split(data):

        #Split the data into training and testing
        X_train = [data[ii] for ii in train_indices]
        X_test = [data[ii] for ii in test_indices]

        Y_train = [labels[ii] for ii in train_indices]
        Y_test = [labels[ii] for ii in test_indices]

        #Fit the classifier
        clf.fit(X_train, Y_train)

        #Print out the results for each iteration
        print("Fold #"+str(fold_number))
        fold_number+=1
        print("TRAIN:")
        print(str(clf.score(X_train, Y_train)*100) + "%")
        avg_train += clf.score(X_train, Y_train)*100
        print("TEST:")
        print(str(clf.score(X_test, Y_test)*100) + "%\n")
        avg_test += clf.score(X_test, Y_test)*100

    #Print out average results
    print(name)
    print("\nAverage train: " + str(avg_train/10))
    print("\nAverage test: " + str(avg_test/10))
    print("\n")

#Uncomment this to save the trained classifier to a file
#joblib.dump(clf, "mlp.pkl")


if __name__ == '__main__':
    mlp_clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(4, 16), random_state=1, activation='logistic')
    kfold("Multi layer perceptron", mlp_clf)

    gbc_clf = GradientBoostingClassifier(n_estimators=500, learning_rate=1.0, max_depth=4, random_state=0, loss='deviance')
    kfold("Gradient Boosted Trees", gbc_clf)

    adb_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
    kfold("Ada Boost", adb_clf)

