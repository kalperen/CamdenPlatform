import datetime
import os
from sklearn.neural_network import MLPClassifier

from kinect_data_processing import get_data

# path of kinect output file
folder = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir + os.sep
                          + os.pardir + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)
dir = os.path.normpath(folder + '/Datasets/kinect_output.csv')


def run(x, y, csv_dir=dir):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1,
                        activation='logistic')
    clf.fit(x, y)
    X_test, y_test = get_data(data_dir=csv_dir)
    output = clf.predict(X_test)
    return output


def generate_api_call(output):
    # Send the gathered data to the cloud platform.
    # The following code will cause the program to crash if you do not have
    # Sapient and sapient-server running when you execute it.
    # Uncomment it if you wish to run locally.

    sitting = output.count('Sitting')
    standing = output.count('Standing')
    laying = output.count('Laying')
    current_dt = datetime.datetime.now()

    body = {
        "sitting": sitting,
        "laying": standing,
        "standing": laying,
        "cameraId": "Kinect",
        "year": current_dt.year,
        "month": current_dt.month,
        "day": current_dt.day,
        "hour": current_dt.hour,
        "minute": current_dt.minute,
        "seconds": current_dt.second
    }


if __name__ == '__main__':
    X_train, y_train = get_data()
    output = run(X_train, y_train)
    # generate_API_call(output)
    print("The output results: ")
    print(output)
