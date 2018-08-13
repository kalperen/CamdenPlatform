import os

from kinect_data_processing import get_data
from sklearn.neural_network import MLPClassifier

X_train, y_train = get_data()

folder = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir + os.sep
                          + os.pardir + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)
csv_dir = os.path.normpath(folder + '/Datasets/kinect_output.csv')

X_test, y_test = get_data(data_dir=csv_dir)

#Define the classifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1,
                    activation='logistic')
#Fit the classifier
clf.fit(X_train, y_train)
#Print out results
print("The output results: ")
x = clf.predict(X_test)
print(x)
