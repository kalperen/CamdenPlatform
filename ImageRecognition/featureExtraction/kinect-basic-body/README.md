# Image Recognition - Kinect

This folder contains an image classifier to determine human body postures from Kinect Data Stream

## References

As a feature extraction technique we use a Microsoft Kinect to create data that will be then labeled in order to be classified.

## Dependencies
1. Microsoft Visual Studio 2017: The project can be opened in Microsoft Visual Studio by clicking BodyBasics-WPF.sln
2. Microsoft Kinect v2
3. Python 3: May require direct call to Python in MainWindow.xaml.cs file

## Generate training data
The TrainModel.xaml.cs file can be renamed to MainWindow.xaml.cs, template to train the data is alreayd in place. 
The dataset should for each label should be trained seperately for the classifier to predict effectively.


### Classification

Change the csv_dir variable in classification/kinect_data_processing.py to match your desired training data set.
files.
Then run python file can be used of to evaluate the classifiers using existing traing data:

```
$ python classification/kinect_evaluation.py
```

### Application

The directories are automatically being handled, the MainWindow.xaml.cs will file the kinect_classification.py file
and execute it through the C# script.

To execute
```
click 'Start' or hit 'F5' on the keyboard while being inside the Microsoft Visual Studio 2017 IDE
```