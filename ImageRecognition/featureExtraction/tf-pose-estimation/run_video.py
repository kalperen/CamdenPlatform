#This file is used to classify the positions of humans in a given video file.

import argparse
import logging
import time
import helpers
import cv2
import numpy as np
import sys
import urllib.request
import json
import datetime

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from sklearn.externals import joblib
logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation Video')
    parser.add_argument('--video', type=str, default='')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution. default=432x368')
    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    parser.add_argument('--showBG', type=bool, default=True, help='False to show skeleton only.')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,help='if provided, resize heatmaps before they are post-processed. default=1.0')
    parser.add_argument('--fps', type=float, default=10)

    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resolution)
    e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    cap = cv2.VideoCapture(args.video)

    frame_counter = 0
    if cap.isOpened() is False:
        print("Error opening video stream or file")
    while cap.isOpened():
        ret_val, image = cap.read()

        try:
            #Invokes the tf openpose feature extractor on the current image
            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
        #Exit when the video ends
        except Exception:
            sys.exit(1)
        #print(frame_counter)
        clf = joblib.load('final.pkl')

        if frame_counter == args.fps:

            array_humans = []
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

            #Count the number of humans who are in each category in the video
            if len(array_humans) > 0:
                sitting, standing, laying = helpers.count_predictions(clf.predict(array_humans))

                currentDT = datetime.datetime.now()
                #Send the gathered data to the cloud platform.
                #The following code will cause the program to crash if you do not have
                #Sapient and sapient-server running when you execute it.
                #Uncomment it if you wish to run locally.
                #--------------------------------------------------------------------------------------------------------#
                body = {
                    "sitting": sitting,
                    "laying": standing,
                    "standing": laying,
                    "cameraId": "1",
                    "year": currentDT.year,
                    "month": currentDT.month,
                    "day": currentDT.day,
                    "hour": currentDT.hour,
                    "minute": currentDT.minute,
                    "seconds": currentDT.second
                }
                req= urllib.request.Request('http://localhost:3000/classifications/addClassification')
                req.add_header('Content-Type', 'application/json; charset=utf-8')
                jsondata = json.dumps(body)
                jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
                req.add_header('Content-Length', len(jsondataasbytes))
                response = urllib.request.urlopen(req, jsondataasbytes)
                #--------------------------------------------------------------------------------------------------------#
        if not args.showBG:
            image = np.zeros(image.shape)
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        cv2.putText(image, "FPS: %f" % (1.0 / (time.time() - fps_time)), (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('tf-pose-estimation result', image)
        fps_time = time.time()
        frame_counter+=1
        if frame_counter > args.fps:
            frame_counter = 0
        if cv2.waitKey(1) == 27:
            break



    cv2.destroyAllWindows()
logger.debug('finished+')
