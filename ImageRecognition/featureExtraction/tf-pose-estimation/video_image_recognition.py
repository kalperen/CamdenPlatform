import argparse
import logging
import time
import os

from tf_pose import common
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from string import digits

dir = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.sep + os.pardir) + "/classification/"
import sys

sys.path.insert(0, dir)
from data_processing import get_data
from sklearn.neural_network import MLPClassifier

logger = logging.getLogger('TfPoseEstimator')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation run')
    parser.add_argument('--video', type=str, default='')
    parser.add_argument('--directory', type=str, default='./images/', help='')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed.'
                             ' default=0x0, Recommends : 432x368 or 656x368 or 1312x736')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')
    parser.add_argument('--framerate', type=int, default=75,
                        help='if provided, resets the framerate to this number. default=75 fps')
    parser.add_argument('--output', type=str)
    args = parser.parse_args()

    w, h = model_wh(args.resize)
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

    cap = cv2.VideoCapture("/Users/video_footage/train_data.mp4")

    if cap.isOpened() is False:
        print("Error opening video stream or file")

    count = 0
    success = True
    while success:
        success, image = cap.read()
        fps = args.framerate
        if count % fps == 0:
            try:
                os.remove("/Users/video_footage/output/")
                print("image deleted")
            except:
                # sleep(5)
                pass

            cv2.imwrite("/Users/video_footage/images/image.jpg", image)
            print("Read a new frame: ", success)

            args = parser.parse_args()

            w, h = model_wh(args.resize)
            if w == 0 or h == 0:
                e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
            else:
                e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

            directory = os.fsencode(args.directory)
            string_humans = ""
            # Goes over a whole directory to generate training data
            for file in os.listdir(directory):
                filename = os.fsdecode(file)

                if filename.endswith(".jpg") and not filename.startswith("."):
                    dir = args.directory + filename
                    image = common.read_imgfile(dir, None, None)
                    if image is None:
                        logger.error('Image can not be read, path=%s' % args.image)
                        continue
                    t = time.time()
                    humans = e.inference(image, resize_to_default=(w > 0 and h > 0),
                                         upsample_size=args.resize_out_ratio)
                    elapsed = time.time() - t

                    label = filename + ","
                    # Strip the all digits from the filename so that we categorize correctly
                    remove_digits = str.maketrans('', '', digits)

                    label = label.translate(remove_digits).replace('.jpg', '')

                    string_human = ""
                    # Go over all the humans in the photo
                    for human in humans:
                        string_human = string_human + label
                        # For every single limb that each human has
                        for i in range(0, 17):
                            try:
                                # record the limb coordinates
                                string_human += str(human.body_parts[i].x) + "," + str(
                                    1 - human.body_parts[i].y) + ","
                            # If there are no coordinates for a certain limb record null
                            except KeyError:
                                string_human += "0.0,0.0,"
                        # Go to the next line after each human in the picture
                        string_human = string_human + "\n"

                    string_humans += string_human
                    # If the user wants to write to an output file
                    if args.output is not None:
                        if os.path.isfile(args.output):
                            f = open(args.output, 'a+')
                            f.write(string_humans)
                            f.close()
                        # If the output file does not exist yet, first populate the string with category headings
                        else:
                            f = open(args.output, 'a+')
                            f.write(
                                "position,noseX,noseY,neckX,neckY,rshoulderX,rshoulderY,relbowX,relbowY,rwristX,"
                                "rwristY,lshoulderX,lshoulderY,lelbowX,lelbowY,lwristX,lwristY,midhipX,midhipY,rhipX,"
                                "rhipY,rkneeX,rkneeY,rankleX,rankleY,lhipX,lhipY,lkneeX,lkneeY,lankleX,lankleY,reyeX,"
                                "reyeY,leyeX,leyeY\n" + string_humans)
                            f.close()
                    X_train, y_train = get_data()
                    X_test, y_test = get_data(data_dir=args.output)
                    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 16), random_state=1,
                                        activation='logistic')
                    clf.fit(X_train, y_train)
                    print("The output results: ")
                    print(clf.predict(X_test))
                    print(" ")
                    try:
                        os.remove(args.output)
                    except:
                        pass

        count += 1
