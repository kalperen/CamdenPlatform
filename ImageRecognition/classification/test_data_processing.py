import unittest
from data_processing import *
import numpy as np
import pandas as pd
import math


def check_nan(dataset):
    contains_nan = False
    for item in dataset:
        if math.isnan(item):
            contains_nan = True
    return contains_nan


class TestDataProcessing(unittest.TestCase):

    def test_clean_up_data(self):
        dataset = pd.read_csv('test_data/test_data_training.csv')

        self.assertIs(type(dataset), pd.core.frame.DataFrame)
        self.assertIs(type(dataset.noseX), pd.core.series.Series)

        before_contains_nan = check_nan(dataset.noseX)
        self.assertTrue(before_contains_nan)

        # call clean_up_data function
        dataset.noseX = clean_up_data(dataset.noseX)
        after_contains_nan = check_nan(dataset.noseX)
        self.assertFalse(after_contains_nan)

    def test_get_data(self):
        cols = ['position', 'noseX', 'noseY', 'neckX', 'neckY', 'rshoulderX', 'rshoulderY', 'relbowX', 'relbowY',
                   'rwristX', 'rwristY', 'lshoulderX', 'lshoulderY', 'lelbowX', 'lelbowY', 'lwristX', 'lwristY',
                   'midhipX', 'midhipY', 'rhipX', 'rhipY', 'rkneeX', 'rkneeY', 'rankleX', 'rankleY', 'lhipX', 'lhipY',
                   'lkneeX', 'lkneeY', 'lankleX', 'lankleY', 'reyeX', 'reyeY']

        train_data = pd.read_csv('test_data/test_data_training.csv', usecols=cols)
        validation_data = pd.read_csv('test_data/test_data_validation.csv', usecols=cols)

        X_train, y_train = get_data(columns=cols, data_dir='test_data/test_data_training.csv')
        X_valid, y_valid = get_data(columns=cols, data_dir='test_data/test_data_validation.csv')

        # check that the columns (cols) and train_data columns are of same length
        self.assertEqual(len(train_data.columns), len(cols))

        # check that X_train and y_train rows length match
        self.assertEqual(len(X_train), len(y_train))

        # extract y from train_data and match the values of within y_train
        y = train_data.position
        y_output = y == y_train
        for item in y_output:
            self.assertTrue(item)

        # check that the columns (cols) and train_data columns are of same length
        self.assertEqual(len(train_data.columns), len(cols))

        # check that X_train and y_train rows length match
        self.assertEqual(len(X_train), len(y_train))

        # extract y from train_data and match the values of within y_train
        y = train_data.position
        y_output = y == y_train
        for item in y_output:
            self.assertTrue(item)

        # test nose_x against train_x noseX values
        train_data.noseX = clean_up_data(train_data.noseX)
        nose_x = np.array(train_data.noseX)
        for i in range(0, len(nose_x)):
            self.assertEqual(train_data.noseX[i], X_train[:, 0][i])

        # Validation tests

        # check that the train_data columns and validation_data columns are of same length
        self.assertEqual(len(validation_data.columns), len(train_data.columns))

        # extract y from validation_data and match the values of within y_valid
        y = validation_data.position
        y_output = y == y_valid
        for item in y_output:
            self.assertTrue(item)

        # test nose_x against train_x noseX values
        validation_data.relbowY = clean_up_data(validation_data.relbowY)
        relbow_y = np.array(validation_data.relbowY)
        for i in range(0, len(relbow_y)):
            self.assertEqual(validation_data.relbowY[i], X_valid[:,7][i])


if __name__ == '__main__':
    unittest.main()
