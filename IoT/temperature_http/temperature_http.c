// Copyright (c) Microsoft. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include <stdlib.h>

#include <stdio.h>
#include <stdint.h>
#include "iot_configs.h"

#include "AzureIoTHub.h"


/*String containing Hostname, Device Id & Device Key in the format:             */
/*  "HostName=<host_name>;DeviceId=<device_id>;SharedAccessKey=<device_key>"    */
static const char* connectionString = IOT_CONFIG_CONNECTION_STRING;

// Define the Model used to serialize
BEGIN_NAMESPACE(Model);

DECLARE_MODEL(TemperatureSensor,
WITH_DATA(ascii_char_ptr, DeviceId),
WITH_DATA(ascii_char_ptr, SensorType),
WITH_DATA(ascii_char_ptr, MeasurementUnit),
WITH_DATA(float, Value)
);

END_NAMESPACE(Model);

static char propText[1024];
static unsigned int messageTrackingId;

void sendCallback(IOTHUB_CLIENT_CONFIRMATION_RESULT result, void* userContextCallback)
{
    (void)printf("Message Id: %u Received.\r\n", messageTrackingId);

    (void)printf("Result Call Back Called! Result is: %s \r\n", ENUM_TO_STRING(IOTHUB_CLIENT_CONFIRMATION_RESULT, result));
}

static void sendMessage(IOTHUB_CLIENT_LL_HANDLE iotHubClientHandle, const unsigned char* buffer, size_t size)
{
    
    IOTHUB_MESSAGE_HANDLE messageHandle = IoTHubMessage_CreateFromByteArray(buffer, size);
    if (messageHandle == NULL)
    {
        printf("unable to create a new IoTHubMessage\r\n");
    }
    else
    {
        if (IoTHubClient_LL_SendEventAsync(iotHubClientHandle, messageHandle, sendCallback, (void*)(uintptr_t)messageTrackingId) != IOTHUB_CLIENT_OK)
        {
            printf("failed to hand over the message to IoTHubClient");
        }
        else
        {
            printf("IoTHubClient accepted the message for delivery\r\n");
        }
        IoTHubMessage_Destroy(messageHandle);
    }
    free((void*)buffer);
    messageTrackingId++;
}

/*this function "links" IoTHub to the serialization library*/
static IOTHUBMESSAGE_DISPOSITION_RESULT IoTHubMessage(IOTHUB_MESSAGE_HANDLE message, void* userContextCallback)
{
    IOTHUBMESSAGE_DISPOSITION_RESULT result;
    const unsigned char* buffer;
    size_t size;
    if (IoTHubMessage_GetByteArray(message, &buffer, &size) != IOTHUB_MESSAGE_OK)
    {
        printf("unable to IoTHubMessage_GetByteArray\r\n");
        result = IOTHUBMESSAGE_ABANDONED;
    }
    else
    {
        /*buffer is not zero terminated*/
        char* temp = malloc(size + 1);
        if (temp == NULL)
        {
            printf("failed to malloc\r\n");
            result = IOTHUBMESSAGE_ABANDONED;
        }
        else
        {
            EXECUTE_COMMAND_RESULT executeCommandResult;
        
            (void)memcpy(temp, buffer, size);
            temp[size] = '\0';
            executeCommandResult = EXECUTE_COMMAND(userContextCallback, temp);
            result =
                (executeCommandResult == EXECUTE_COMMAND_ERROR) ? IOTHUBMESSAGE_ABANDONED :
                (executeCommandResult == EXECUTE_COMMAND_SUCCESS) ? IOTHUBMESSAGE_ACCEPTED :
                IOTHUBMESSAGE_REJECTED;
            free(temp);
        }
    }
    return result;
}

void http_run(void)
{
    if (platform_init() != 0)
    {
        printf("Failed to initialize the platform.\r\n");
    }
    else
    {
        if (serializer_init(NULL) != SERIALIZER_OK)
        {
            (void)printf("Failed on serializer_init\r\n");
        }
        else
        {
            //create the iot hub client handler
            IOTHUB_CLIENT_LL_HANDLE iotHubClientHandle = IoTHubClient_LL_CreateFromConnectionString(connectionString, HTTP_Protocol);
            int avgWindSpeed = 10;
            float minTemperature = 20.0;
            float minHumidity = 60.0;

            srand((unsigned int)time(NULL));

            if (iotHubClientHandle == NULL)
            {
                (void)printf("Failed on IoTHubClient_LL_Create\r\n");
            }
            else
            {
                TemperatureSensor* myWeather;


#ifdef SET_TRUSTED_CERT_IN_SAMPLES
                // For mbed add the certificate information
                if (IoTHubClient_LL_SetOption(iotHubClientHandle, "TrustedCerts", certificates) != IOTHUB_CLIENT_OK)
                {
                    (void)printf("failure to set option \"TrustedCerts\"\r\n");
                }
#endif // SET_TRUSTED_CERT_IN_SAMPLES

                myWeather = CREATE_MODEL_INSTANCE(Model, TemperatureSensor);
                if (myWeather == NULL)
                {
                    (void)printf("Failed on CREATE_MODEL_INSTANCE\r\n");
                }
                else
                {
                    //set message callbacks
                    if (IoTHubClient_LL_SetMessageCallback(iotHubClientHandle, IoTHubMessage, myWeather) != IOTHUB_CLIENT_OK)
                    {
                        printf("unable to IoTHubClient_SetMessageCallback\r\n");
                    }
                    else
                    {
                        while (true){
                          int sensorValue = analogRead(1); 
    
                          float voltage = sensorValue * (3300/1024); // in milliVolt 
     
                          float temperature = (voltage - 500 ) / 10;
                          
                          myWeather->DeviceId = "MyMKR1000";
                          myWeather->SensorType = "Temperature";
                          myWeather->MeasurementUnit = "C";
                          myWeather->Value = temperature;
                          {
                              unsigned char* destination;
                              size_t destinationSize;
                              if (SERIALIZE(&destination, &destinationSize, myWeather->DeviceId, myWeather->SensorType, myWeather->MeasurementUnit, myWeather->Value) != CODEFIRST_OK)
                              {
                                  (void)printf("Failed to serialize\r\n");
                              }
                              else
                              {
                                sendMessage(iotHubClientHandle, destination, destinationSize);
                              }
                          }
                          IOTHUB_CLIENT_STATUS status;
  
                          while ((IoTHubClient_LL_GetSendStatus(iotHubClientHandle, &status) == IOTHUB_CLIENT_OK) && (status == IOTHUB_CLIENT_SEND_STATUS_BUSY))
                          {
                              IoTHubClient_LL_DoWork(iotHubClientHandle);
                              ThreadAPI_Sleep(100);
                          }
                          ThreadAPI_Sleep(5000);
                        }
                    }

                    DESTROY_MODEL_INSTANCE(myWeather);
                }
                IoTHubClient_LL_Destroy(iotHubClientHandle);
            }
            serializer_deinit();
        }
        platform_deinit();
    }
}

void run(void)
{
    http_run();
}

