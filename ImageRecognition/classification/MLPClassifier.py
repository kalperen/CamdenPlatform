from data_processing import get_data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

data, labels = get_data()

# print(data.shape)
# print(target.shape)
# X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.4, random_state=0)
#
#
# print(X_train.shape)
# print(y_train.shape)
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1, activation='logistic')
# clf.fit(X_train, y_train)
# print("\nTRAIN:")
# print(str(clf.score(X_train, y_train)*100) + "%")
# print("\nTEST:")
# print(str(clf.score(X_test, y_test)*100) + "%")

avg_train = 0
avg_test = 0
fold_number=0
from sklearn.model_selection import KFold
kf = KFold(n_splits=10, shuffle=True)
for train_indices, test_indices in kf.split(data):
    
    X_train = [data[ii] for ii in train_indices]
    X_test = [data[ii] for ii in test_indices]

    Y_train = [labels[ii] for ii in train_indices]
    Y_test = [labels[ii] for ii in test_indices]

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1, activation='logistic')
    clf.fit(X_train, Y_train)
    print("Fold #"+str(fold_number))
    fold_number+=1
    print("TRAIN:")
    print(str(clf.score(X_train, Y_train)*100) + "%")
    avg_train += clf.score(X_train, Y_train)*100
    print("TEST:")
    print(str(clf.score(X_test, Y_test)*100) + "%\n")
    avg_test += clf.score(X_test, Y_test)*100

print("\nAverage train: " + str(avg_train/10))
print("\nAverage test: " + str(avg_test/10))
