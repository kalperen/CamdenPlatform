#include <AzureIoTUtility.h>

// Copyright (c) Microsoft. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include "iot_configs.h"

#include <AzureIoTHub.h>

#include <AzureIoTProtocol_HTTP.h>

#include "temperature.h"
#include "samd/sample_init.h"

static char ssid[] = IOT_CONFIG_WIFI_SSID;
static char pass[] = IOT_CONFIG_WIFI_PASSWORD;

void setup() {
    sample_init(ssid, pass);
}

static bool done = false;
void loop() {
    if (!done)
    {
        run();
        done = true;
    }
    else
    {
      delay(5000);
    }
}

