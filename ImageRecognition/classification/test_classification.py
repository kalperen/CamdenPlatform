import unittest

import MLPClassifierKinect as MLP


class TestDataProcessing(unittest.TestCase):

    def test_kinect_classification_random_data(self):

        X_train, y_train = MLP.get_data(data_dir='test_data/test_kinect_training.csv')
        self.assertEqual(X_train.size, 4125)
        self.assertEqual(y_train.size, 55)

        output = MLP.run(X_train, y_train, csv_dir='test_data/test_kinect_validation.csv')
        # check that correct number of output values are being produced
        self.assertEqual(output.size, 17)

        for i in output:
            # check that only valid output is being passed
            position = (i == "Standing" or i == "Sitting" or i == "Laying")
            self.assertTrue(position)

    def test_kinect_classification_trained_data(self):

        # retrieve original trained data
        X_train, y_train = MLP.get_data(data_dir='../Datasets/kinect_training.csv')
        # check correct data has been loaded and correct format of values
        self.assertEqual(X_train.dtype, 'float64')
        self.assertTrue('Sitting' in y_train)
        self.assertTrue('Standing' in y_train)
        self.assertTrue('Laying' in y_train)

        output = MLP.run(X_train, y_train, csv_dir='test_data/test_kinect_validation.csv')

        # check that correct number of output values are being produced
        self.assertEqual(output.size, 17)

        # load the y_test data so values can be compared
        X_test, y_test = MLP.get_data(data_dir='test_data/test_kinect_validation.csv')
        # check each output value against original value to see if correctly being predicted
        for i in range(0, len(y_test)):
            # check positions matching
            self.assertEqual(y_test[i], output[i])


if __name__ == '__main__':
    unittest.main()
