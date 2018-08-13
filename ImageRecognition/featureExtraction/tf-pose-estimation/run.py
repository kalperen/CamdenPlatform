#This file is used for feature extraction purposes.
#Place all image files that you wish to extract features from into a subdirectory
#Make sure to name every image file according to its category. For example an image
#Where the humans are sitting could be named "sitting123543.jpg".
#And run this script on it. This will generate a csv file that can then be used
#To train a classifier.

import argparse
import logging
import sys
import time
import os
import helpers

from tf_pose import common
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from string import digits

logger = logging.getLogger('TfPoseEstimator')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation run')
    parser.add_argument('--image', type=str, default='./images/p1.jpg')
    parser.add_argument('--model', type=str, default='cmu', help='cmu / mobilenet_thin')

    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')
    parser.add_argument('--directory', type=str, default='./images/', help='')
    parser.add_argument('--output', type=str)

    args = parser.parse_args()

    w, h = model_wh(args.resize)
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

    print(args.directory)
    directory = os.fsencode(args.directory)
    print(directory)
    string_humans =""

    #Goes over a whole directory to generate training data
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".jpg") and not filename.startswith("."):
            dir = "./images/" + filename
            image = common.read_imgfile(dir, None, None)
            if image is None:
                logger.error('Image can not be read, path=%s' % args.image)
                continue
            t = time.time()

            #Invokes the tf openpose feature extractor on the current image
            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
            elapsed = time.time() - t

            #The file name is used as the label the following code will take an image filename such
            #as "laying123.jpg" and interpret it as the "laying" category in the produced feature extraction.
            label = filename + ","

            #Strip the all digits from the filename so that we categorize correctly
            remove_digits = str.maketrans('', '', digits)

            label = label.translate(remove_digits).replace('.jpg', '')

            string_human = ""
            #Go over all the humans in the photo
            for human in humans:
                current_human = '' + label
                #For every single limb that each human has
                for i in range(0, 17):
                    try:
                        #record the limb coordinates
                        current_human += str(human.body_parts[i].x) + "," + str(
                        1-human.body_parts[i].y) + ","
                    #If there are no coordinates for a certain limb record null
                    except KeyError:
                        current_human += "0.0,0.0,"
                #remove the trailing comma from the string.
                current_human = current_human[:-1]
                #Improve the generated feature extraction by removing unclear data points
                if helpers.clean_string_data(current_human) is None:
                    current_human = ''
                else:
                    current_human += "\n"
                #Add the current human in the picture to the string of humans in this picture
                string_human += current_human
                current_human = ''
            #Add all humans  in this picture to the string of all humans in all pictures in this subdirectory
            string_humans += string_human

    #Write to an output file designated by the user.
    if args.output is not None:
        if os.path.isfile(args.output):
            f = open(args.output,'a+')
            f.write(string_human)
            f.close()
        #If the output file does not exist yet, first populate the string with category headings
        else:
            f = open(args.output,'a+')
            f.write("position,noseX,noseY,neckX,neckY,rshoulderX,rshoulderY,relbowX,relbowY,rwristX,rwristY,lshoulderX,lshoulderY,lelbowX,lelbowY,lwristX,lwristY,midhipX,midhipY,rhipX,rhipY,rkneeX,rkneeY,rankleX,rankleY,lhipX,lhipY,lkneeX,lkneeY,lankleX,lankleY,reyeX,reyeY,leyeX,leyeY\n"+string_humans)
            f.close()
