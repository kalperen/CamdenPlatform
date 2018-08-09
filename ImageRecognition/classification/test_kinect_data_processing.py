import unittest
from kinect_data_processing import *
import numpy as np
import pandas as pd
import math


def check_nan(dataset):
    contains_nan = False
    dataset = dataset.astype(float).astype('float64')
    for item in dataset:
        if math.isnan(item):
            contains_nan = True
    return contains_nan


cols = ['Position', 'SpineBaseX', 'SpineBaseY', 'SpineBaseZ', 'SpineMidX', 'SpineMidY', 'SpineMidZ', 'NeckX', 'NeckY',
        'NeckZ', 'HeadX', 'HeadY', 'HeadZ', 'ShoulderLeftX', 'ShoulderLeftY', 'ShoulderLeftZ', 'ElbowLeftX',
        'ElbowLeftY', 'ElbowLeftZ', 'WristLeftX', 'WristLeftY', 'WristLeftZ', 'HandLeftX', 'HandLeftY', 'HandLeftZ',
        'ShoulderRightX', 'ShoulderRightY', 'ShoulderRightZ', 'ElbowRightX', 'ElbowRightY', 'ElbowRightZ',
        'WristRightX', 'WristRightY', 'WristRightZ', 'HandRightX', 'HandRightY', 'HandRightZ', 'HipLeftX', 'HipLeftY',
        'HipLeftZ', 'KneeLeftX', 'KneeLeftY', 'KneeLeftZ', 'AnkleLeftX', 'AnkleLeftY', 'AnkleLeftZ', 'FootLeftX',
        'FootLeftY', 'FootLeftZ', 'HipRightX', 'HipRightY', 'HipRightZ', 'KneeRightX', 'KneeRightY', 'KneeRightZ',
        'AnkleRightX', 'AnkleRightY', 'AnkleRightZ', 'FootRightX', 'FootRightY', 'FootRightZ', 'SpineShoulderX',
        'SpineShoulderY', 'SpineShoulderZ', 'HandTipLeftX', 'HandTipLeftY', 'HandTipLeftZ', 'ThumbLeftX', 'ThumbLeftY',
        'ThumbLeftZ', 'HandTipRightX', 'HandTipRightY', 'HandTipRightZ', 'ThumbRightX', 'ThumbRightY', 'ThumbRightZ']


class TestDataProcessing(unittest.TestCase):

    def test_clean_up_data(self):
        dataset = pd.read_csv('test_data/test_kinect_training.csv', usecols=cols)

        self.assertIs(type(dataset), pd.core.frame.DataFrame)
        self.assertIs(type(dataset.SpineBaseY), pd.core.series.Series)

        before_contains_nan = check_nan(dataset.SpineBaseY)
        self.assertTrue(before_contains_nan)

        # call clean_up_data function
        dataset.SpineBaseY = clean_up_data(dataset.SpineBaseY)
        after_contains_nan = check_nan(dataset.SpineBaseY)
        self.assertFalse(after_contains_nan)

    def test_get_data_train(self):
        test_dataset = pd.read_csv('test_data/test_kinect_training.csv', usecols=cols)
        X_train, y_train = get_data(columns=cols, data_dir='test_data/test_kinect_training.csv')

        # check that the columns (cols) and train_data columns are of same length
        self.assertEqual(len(test_dataset.columns), len(cols))
        # check that X_train and y_train rows length match
        self.assertEqual(len(X_train), len(y_train))

        # extract y from train_data and match the values of within y_train
        y = test_dataset.Position
        y_output = y == y_train
        for item in y_output:
            self.assertTrue(item)

        # test HeadX against train_x HeadX values
        head_x = np.array(test_dataset.HeadX)
        for i in range(0, len(head_x)):
            self.assertEqual(test_dataset.HeadX[i], X_train[:,9][i])

