import argparse
import logging
import os
import sys
import time
from string import digits

import numpy as np
from lifting.prob_model import Prob3dPose
from tf_pose import common
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
    # os.chdir("..")
    parser = argparse.ArgumentParser(description='tf-pose-estimation run_3d')
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
    print(directory)
    string_humans = ""
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".jpg") and not filename.startswith("."):
            dir = args.directory + filename
            # estimate human poses from a single image !
            image = common.read_imgfile(dir, None, None)
            if image is None:
                logger.error('Image can not be read, path=%s' % dir)
                sys.exit(-1)
            t = time.time()
            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
            elapsed = time.time() - t

            # print human joints
            print("Number of people in image: ", len(humans))

            pose_2d_mpiis = []
            visibilities = []
            standard_w = 432
            standard_h = 368
            for human in humans:
                pose_2d_mpii, visibility = common.MPIIPart.from_coco(human)
                pose_2d_mpiis.append([(int(x * standard_w + 0.5), int(y * standard_h + 0.5)) for x, y in pose_2d_mpii])
                visibilities.append(visibility)

            pose_2d_mpiis = np.array(pose_2d_mpiis)

            # shahroz code
            poseLifting = Prob3dPose('./lifting/models/prob_model_params.mat')
            visibilities = np.array(visibilities)
            transformed_pose2d, weights = poseLifting.transform_joints(pose_2d_mpiis, visibilities)
            pose_3d = poseLifting.compute_3d(transformed_pose2d, weights)

            label = filename + ","
            # Strip the all digits from the filename so that we categorize correctly
            remove_digits = str.maketrans('', '', digits)
            label = label.translate(remove_digits).replace('.jpg', '')

            string_human = ""
            # Go over all the humans in the photo
            for human in pose_3d:
                string_human = string_human + label
                for i in range(0, 17):
                    try:
                        # print("x:" + str(human[0][i]) + ", y:" + str(human[1][i]) + ", z:" + str(human[2][i]))
                        string_human += str(human[0][i]) + "," + str(human[1][i]) + "," + str(human[2][i]) + ","

                    except KeyError:
                        string_human += "0.0,0.0,0.0"

                string_human = string_human + "\n"
            string_humans += string_human
            logger.info('inference image: %s in %.4f seconds.' % (dir, elapsed))

            image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

            '''
            import matplotlib.pyplot as plt
            fig = plt.figure()
            a = fig.add_subplot(1, 1, 1)
            a.set_title('Result')
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            tmp2 = e.pafMat.transpose((2, 0, 1))
            tmp2_odd = np.amax(np.absolute(tmp2[::2, :, :]), axis=0)
            tmp2_even = np.amax(np.absolute(tmp2[1::2, :, :]), axis=0)

            plt.show()
            '''

    if args.output is not None:
        if os.path.isfile(args.output):
            f = open(args.output, 'a+')
            f.write(string_humans)
            f.close()
        # If the output file does not exist yet, first populate the string with category headings
        else:
            f = open(args.output, 'a+')
            f.write(
                "position,noseX,noseY,noseZ,neckX,neckY,neckZ,rshoulderX,rshoulderY,rshoulderZ,relbowX,relbowY,relbowZ,"
                "rwristX,rwristY,rwristZ,lshoulderX,lshoulderY,lshoulderZ,lelbowX,lelbowY,lelbowZ,lwristX,lwristY,"
                "lwristZ,midhipX,midhipY,midhipZ,rhipX,rhipY,rhipZ,rkneeX,rkneeY,rkneeZ,rankleX,rankleY,rankleZ,lhipX,"
                "lhipY,lhipZ,lkneeX,lkneeY,lkneeZ,lankleX,lankleY,lankleZ,reyeX,reyeY,reyeZ,leyeX,leyeY,leyeZ\n"
                + string_humans)
            f.close()
