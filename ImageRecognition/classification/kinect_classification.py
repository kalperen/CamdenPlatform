import datetime
import json
import os
import urllib.request
import sys
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

from kinect_data_processing import get_data

# path of kinect output file
folder = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir + os.sep
                          + os.pardir + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir)
dir = os.path.normpath(folder + '/Datasets/kinect_output.csv')


def run(x, y, csv_dir=dir):
    # clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1,
                       # activation='logistic')

    clf = GradientBoostingClassifier(n_estimators=500, learning_rate=1.0, max_depth=4, random_state=0,
                                         loss='deviance')
    clf.fit(x, y)
    X_test, y_test = get_data(data_dir=csv_dir)
    output = clf.predict(X_test)
    return output


def generate_api_call(output, cloud=True):
    # Send the gathered data to the cloud platform.
    # The following code will cause the program to crash if you do not have
    # Sapient and sapient-server running when you execute it.
    # Uncomment it if you wish to run locally.

    # convert from np.array to list
    output = output.tolist()

    # count number of appearances of a particular position in a list
    sitting = output.count('Sitting')
    standing = output.count('Standing')
    laying = output.count('Laying')


    current_dt = datetime.datetime.now()

    body = {
        "sitting": sitting,
        "laying": laying,
        "standing": standing,
        "cameraId": "Kinect",
        "year": current_dt.year,
        "month": current_dt.month,
        "day": current_dt.day,
        "hour": current_dt.hour,
        "minute": current_dt.minute,
        "seconds": current_dt.second
    }
    print(body)
    if (cloud):
        req = urllib.request.Request('http://localhost:3000/classifications/addClassification')
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        urllib.request.urlopen(req, jsondataasbytes)


if __name__ == '__main__':
    X_train, y_train = get_data()
    output = run(X_train, y_train)
    generate_api_call(output)
    #print("The output results: ")
    #print(output)
