import unittest
import kinect_classification as MLP_Kinect


class TestDataProcessing(unittest.TestCase):

    def test_kinect_classification_random_data(self):
        # retrieve kinect mock data
        X_train, y_train = MLP_Kinect.get_data(data_dir='test_data/test_kinect_training.csv')
        self.assertEqual(X_train.size, 4125)
        self.assertEqual(y_train.size, 55)

        output = MLP_Kinect.run(X_train, y_train, csv_dir='test_data/test_kinect_validation.csv')
        # check that correct number of output values are being produced
        self.assertEqual(output.size, 17)

        for i in output:
            # check that only valid output is being passed
            position = (i == "Standing" or i == "Sitting" or i == "Laying")
            self.assertTrue(position)

    def test_kinect_classification_trained_data(self):

        # retrieve original kinect trained data
        X_train, y_train = MLP_Kinect.get_data(data_dir='../Datasets/kinect_training.csv')
        # check correct data has been loaded and correct format of values
        self.assertEqual(X_train.dtype, 'float64')
        self.assertTrue('Sitting' in y_train)
        self.assertTrue('Standing' in y_train)
        self.assertTrue('Laying' in y_train)

        output = MLP_Kinect.run(X_train, y_train, csv_dir='test_data/test_kinect_validation.csv')

        # check that correct number of output values are being produced
        self.assertEqual(output.size, 17)

        # load the y_test data so values can be compared
        X_test, y_test = MLP_Kinect.get_data(data_dir='test_data/test_kinect_validation.csv')

        # check each output value against original value to see if correctly being predicted
        for i in range(0, len(y_test)):
            # check positions matching
            self.assertEqual(y_test[i], output[i])

        # check that only valid output is being passed
        for i in output:
            # check that only valid output is being passed
            position = (i == "Standing" or i == "Sitting" or i == "Laying")
            self.assertTrue(position)

    def test_kinect_classification_random_data(self):

        from sklearn.neural_network import MLPClassifier

        # retrieve mock classification data
        from data_processing import get_data
        X_train, y_train = get_data(data_dir='test_data/test_data_training.csv')

        # check correct data has been loaded and correct format of values
        self.assertEqual(X_train.dtype, 'float64')
        self.assertTrue('sitting' in y_train)
        self.assertTrue('standing' in y_train)
        self.assertTrue('laying' in y_train)

        # use default settings applied in script
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1,
                            activation='logistic')
        clf.fit(X_train, y_train)
        X_test, y_test = get_data(data_dir='test_data/test_data_validation.csv')
        output = clf.predict(X_test)

        # check that only valid output is being passed
        for i in output:
            # check that only valid output is being passed
            position = (i == "standing" or i == "sitting" or i == "laying")
            self.assertTrue(position)


if __name__ == '__main__':
    unittest.main()
