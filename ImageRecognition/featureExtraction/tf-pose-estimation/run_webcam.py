#This file is used to classify the positions of humans in a given live video feed.

import argparse
import logging
import time

import cv2
import numpy as np

from sklearn.externals import joblib

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)

    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resize)
    if w > 0 and h > 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    logger.debug('cam read+')
    cam = cv2.VideoCapture(args.camera)
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

    array_humans = []

    clf = joblib.load('mlp.pkl')
    while True:
        ret_val, image = cam.read()

        logger.debug('image process+')
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)

        #Go over all the humans in the photo
        for human in humans:
            array_human = []
            #For every single limb that each human has
            for i in range(0, 16):
                try:
                    #record the limb coordinates
                    array_human.append(human.body_parts[i].x)
                    array_human.append(human.body_parts[i].y)
                #If there are no coordinates for a certain limb record null
                except KeyError:
                    array_human.append(0.0)
                    array_human.append(0.0)
            #Improve the generated feature extraction by removing unclear data points
            if helpers.clean_data(array_human) is None:
                array_human = []
            else:
                array_humans.append(array_human)
                array_human = []

        #Print the current classification
        if len(array_humans) > 0:
            print(clf.predict(array_humans))
            #
            # sitting, standing, laying = helpers.count_predictions(clf.predict(array_humans))
            #
            # currentDT = datetime.datetime.now()
            # #Send the gathered data to the cloud platform.
            # #The following code will cause the program to crash if you do not have
            # #Sapient and sapient-server running when you execute it.
            # #Uncomment it if you wish to run locally.
            # #--------------------------------------------------------------------------------------------------------#
            # body = {
            #     "sitting": sitting,
            #     "laying": standing,
            #     "standing": laying,
            #     "cameraId": "1",
            #     "year": currentDT.year,
            #     "month": currentDT.month,
            #     "day": currentDT.day,
            #     "hour": currentDT.hour,
            #     "minute": currentDT.minute,
            #     "seconds": currentDT.second
            # }
            # req= urllib.request.Request('http://localhost:3000/classifications/addClassification')
            # req.add_header('Content-Type', 'application/json; charset=utf-8')
            # jsondata = json.dumps(body)
            # jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
            # req.add_header('Content-Length', len(jsondataasbytes))
            # response = urllib.request.urlopen(req, jsondataasbytes)
            # #--------------------------------------------------------------------------------------------------------#

        del array_humans[:]
        logger.debug('postprocess+')
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        logger.debug('show+')
        cv2.putText(image,
                    "FPS: %f" % (1.0 / (time.time() - fps_time)),
                    (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps_time = time.time()
        if cv2.waitKey(1) == 27:
            break
        logger.debug('finished+')

    cv2.destroyAllWindows()
