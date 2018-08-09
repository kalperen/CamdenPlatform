import unittest
from kinect_data_processing import *
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
