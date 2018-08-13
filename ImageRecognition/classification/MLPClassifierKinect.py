import os
from kinect_data_processing import get_data
from sklearn.neural_network import MLPClassifier

# path of kinect output file
folder = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir + os.sep
                          + os.pardir + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)
dir = os.path.normpath(folder + '/Datasets/kinect_output.csv')


def run(x, y, csv_dir=dir):
    X_test, y_test = get_data(data_dir=csv_dir)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1,
                        activation='logistic')
    clf.fit(x, y)
    print("The output results: ")
    x = clf.predict(X_test)
    print(x)


if __name__ == '__main__':
    X_train, y_train = get_data()
    run(X_train, y_train)
