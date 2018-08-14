# Image Recognition

This folder contains an image classifier to determine human body postures from live video footage.

## References

As a feature extraction technique we use a [TensorFlow implementation](https://github.com/ildoonet/tf-pose-estimation) of the [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) library. We plan to modify this implementation to automatically
create data that will be then labeled in order to be classified.

## Dependencies
1. [tf-openpose](https://github.com/ildoonet/tf-pose-estimation): Follow instructions in the repository for Installation
2. python3
3. [tensorflow 1.4.1+](https://www.tensorflow.org/install/)
4. opencv3, protobuf
5. [Conda](https://conda.io/docs/user-guide/install/index.html)

## Installation

### Feature extraction

We recommend creating a new Conda Environment and installing all the requirements as follows:

```
$ conda create -n tfpose python=3.6 pip
$ activate tfpose (or on MacOs: source activate tfpose)
$ pip install -r requirements.txt
$ pip install tensorflow
$ pip install opencv-python
$ brew install swig
$ cd tf_pose/pafprocess
$ swig -python -c++ pafprocess.i && python setup.py build_ext --inplace
```

## Usage

### Feature extraction

Create a folder named images in featureExtraction/tf-pose-estimation/. Place all the images that you
will be using for training in your model and that you want features to be extracted from.
Make sure to name each image according to its label. For example images containing humans that
are laying down should be named "laying1.jpg", "laying2.jpg" etc...

```
$ cd featureExtraction/tf-pose-estimation/
$ mkdir images
```

This command will loop over all the images in images/ folder and write the extracted features
into data.csv

```
$ python run.py --output=data.csv
```

### Classification

Change the csv_dir variable in classification/data_processing.py to match your desired training data set.
files. Then run one of the following:

```
$ python classification/MLPClassifier.py
$ python classification/GradientBoostedTrees.py
$ python classification/AdaBoost.py
```
These will generate .pkl files in the directory that can then be used in the application.

### Application

Navigate back to featureExtraction/tf-pose-estimation.
Copy your generated .pkl file into this subdirectory. Depending on which file you want to run
make sure you change the 'desired.pkl' in the "clf = joblib.load('desired.pkl')" line to your
previously generated pkl file.

Single image
```
$ python run.py --image=./images/p1.jpg
```

Realtime Webcam
```
$ python run_webcam.py --camera=0
```

Pre-saved Video
```
$ python run_video.py --video=video.mp4
```

You can also add the --model and --resolution arguments to the above commands.
This might affect both precision and runtime depending on the power of your GPU.
