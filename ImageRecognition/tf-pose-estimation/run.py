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

    args = parser.parse_args()

    w, h = model_wh(args.resize)
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

    # estimate human poses from a single image !
    print("args image")
    print(args.image)
    image = common.read_imgfile(args.image, None, None)
    if image is None:
        logger.error('Image can not be read, path=%s' % args.image)
        sys.exit(-1)
    t = time.time()
    humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
    elapsed = time.time() - t

    logger.info('inference image: %s in %.4f seconds.' % (args.image, elapsed))

    image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

    directory = os.fsencode(args.directory)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            dir = "./images/" + filename
            image = common.read_imgfile(dir, None, None)
            if image is None:
                logger.error('Image can not be read, path=%s' % args.image)
                continue
            t = time.time()
            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
            elapsed = time.time() - t
            #print(humans)

            # applying data structure
            list_humans = []
            for human in humans:
                list_human = []
                for i in human.body_parts:
                    joint_coord = []
                    joint_coord.append(human.body_parts[i].part_idx)
                    joint_coord.append(human.body_parts[i].x)
                    joint_coord.append(human.body_parts[i].y)
                    list_human.append(joint_coord)
                list_humans.append(list_human)
            print(list_humans)

    import matplotlib.pyplot as plt

    fig = plt.figure()
    a = fig.add_subplot(1, 1, 1)
    a.set_title('Result')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.show()
