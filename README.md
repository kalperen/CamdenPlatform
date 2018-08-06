[![Build Status](https://travis-ci.com/kalperen/CamdenPlatform.svg?branch=master)](https://travis-ci.com/kalperen/CamdenPlatform)
[![codecov](https://codecov.io/gh/kalperen/CamdenPlatform/branch/master/graph/badge.svg)](https://codecov.io/gh/kalperen/CamdenPlatform)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7b4b26ff2c0a4c0caddb1f6ab18eb13f)](https://www.codacy.com/app/kalperen/CamdenPlatform?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kalperen/CamdenPlatform&amp;utm_campaign=Badge_Grade)

# CamdenPlatform
Cloud based IOT Platform with integrated AI

## Image Detection Features
- **Functionality**:
    - **2D real-time multi-person body posture classification through camera feed**:
      - 18 Keypoints
    - **2D real-time multi-person body posture classification through depth sensor feed (Microsoft Kinect)**:
        - Example
- **Input**: Image, video, webcam, Kinect.
- **Output**: Currently three body postures are supported: "Standing", "Sitting", and "Laying"
- **OS**: Ubuntu (14, 16), Windows (8, 10), Mac OSX, Nvidia TX2.

## Platform Features
- **Functionality**:
  - **Cloud based sensor mesh managment platformx**:
    - Easy to set up and configure web app that allows users to add, configure and analyse data from a sensor mesh.

## Quick Start

- To install and deploy the image recognition module see [imageRecognition/README.md](imageRecognition/README.md)
- To install and deploy the sensor mesh managment platform see [Sapient/README.md](Sapient/README.md) and [sapient-server/README.md](sapient-server/README.md)
- To configure an Arduino based sensor see [Iot/README.md](Iot/README.md)
