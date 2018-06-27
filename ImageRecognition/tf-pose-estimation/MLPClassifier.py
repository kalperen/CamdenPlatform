from data_processing import get_data
import pandas as pd
from sklearn.neural_network import MLPClassifier

X_train, y_train, X_valid, y_valid, train_data, validation_data = get_data()
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X_train, y_train)
print(clf.predict(X_valid))
