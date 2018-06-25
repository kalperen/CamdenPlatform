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

For feature extraction:
### Single Image
```
$ python run.py --model=mobilenet_thin --resize=432x368 --image=./images/p1.jpg
```

### Realtime Webcam

```
$ python run_webcam.py --model=mobilenet_thin --resize=432x368 --camera=0
```

# Warning: This is repository is not completed yet
