# IoT

This folder contains the code that runs on the sensors that will connect to our platform.

## Installation

This guide is meant for use with the Arduino MKR1000 and the Arduino IDE (version 1.6.8 and later). The following steps are valid for all sketches in this repository.

1. Open the Arduino IDE and install the following libraries using the ```Library Manager```, which can be accessed via ```Sketch -> Include Library -> Managed Libraries ...```
  * ```WiFi101```
  * ```RTCZero```
  * ```AzureIoT```

2. Flash the root certificate of the Azure IoT hub host, ```CamdenHub.azure-devices.net``` found in Connection String from [earlier](#beforebegin), using the instructions available on the ["Firmware/Certificates updater for the Arduino Wifi 101 Shield"](https://github.com/arduino-libraries/WiFi101-FirmwareUpdater#usage) page. Running this step can be problematic on MacOs machines, we suggest proceeding on a Windows computer for this part.

3. Import the sketch, verify and upload in to the MKR1000 on the Arduino IDE. In case of errors, an alternative to using the IDE (again for MacOs related problems) is using the online Arduino editor, which has all the functionalities of the Desktop IDE.

## Usage

Once the sketch is uploaded on the MKR1000, every time the MKR1000 is connected to power, the sketch will start to run and to continuosily execute the loop function.