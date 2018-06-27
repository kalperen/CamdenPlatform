import argparse
import logging
import sys
import time
import os

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

    directory = os.fsencode(args.directory)

    #if directory.endswith(".csv"):

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
            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
            elapsed = time.time() - t

            string_human = filename + ","
            #Strip the all digits from the filename so that we categorize correctly
            remove_digits = str.maketrans('', '', digits)
            string_human = string_human.translate(remove_digits).replace('.jpg', '')

            #Go over all the humans in the photo
            for human in humans:
                #For every single limb that each human has
                for i in range(0, 17):
                    try:
                        #record the limb coordinates
                        string_human += str(human.body_parts[i].x) + "," + str(
                        1-human.body_parts[i].y) + ","
                    #If there are no coordinates for a certain limb record null
                    except KeyError:
                        string_human += "0.0,0.0,"
                #Go to the next line after each human in the picture
                string_human = string_human + "\n"
            #If the user wants to write to an output file
            if args.output is not None:
                if os.path.isfile(args.output):
                    f = open(args.output,'a+')
                    f.write(string_human)
                    f.close()
                #If the output file does not exist yet, first populate the string with category headings
                else:
                    f = open(args.output,'a+')
                    f.write("position, noseX, noseY, neckX, neckY, rshoulderX, rshoulderY, relbowX, relbowY, rwristX, rwristY, lshoulderX, lshoulderY, lelbowX, lelbowY, lwristX, lwristY, midhipX, midhipY, rhipX, rhipY, rkneeX, rkneeY, rankleX, rankleY, lhipX, lhipY, lkneeX, lkneeY, lankleX, lankleY, reyeX, reyeY, leyeX, leyeY, rearX, rearY\n"+string_human)
                    f.close()

#def csv_output:
