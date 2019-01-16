from data_processing import get_data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import ensemble
from sklearn.externals import joblib
data, labels = get_data()


print("Multi layer perceptron")
avg_train = 0
avg_test = 0
fold_number=0

#Do K-Fold cross validation on the data
from sklearn.model_selection import KFold
kf = KFold(n_splits=10, shuffle=True)
for train_indices, test_indices in kf.split(data):

    #Split the data into training and testing
    X_train = [data[ii] for ii in train_indices]
    X_test = [data[ii] for ii in test_indices]

    Y_train = [labels[ii] for ii in train_indices]
    Y_test = [labels[ii] for ii in test_indices]

    #Define the classifier
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(32, 16, 8, 4, 2), random_state=1, activation='tanh',learning_rate='constant', learning_rate_init=0.003)

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
print("\nAverage train: " + str(avg_train/10))
print("\nAverage test: " + str(avg_test/10))

#Uncomment this to save the trained classifier to a file
#joblib.dump(clf, "mlp.pkl")
