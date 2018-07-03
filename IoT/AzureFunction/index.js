module.exports = function (context, IoTHubMessages) {
    context.log(`JavaScript eventhub trigger function called for message array: ${JSON.stringify(IoTHubMessages)}`);

    var value = 0.0;
    var deviceId = "";
    var sensorType = "";
    var measurementUnit = "";
    var d = new Date();

    IoTHubMessages.forEach(message => {
        context.log(`Processed message: ${message}`);
        value = message.Value;
        deviceId = message.DeviceId;
        sensorType = message.SensorType;
        measurementUnit = message.MeasurementUnit;
    });

    var output = {
        "deviceId": deviceId,
        "measurementUnit": measurementUnit,
        "measurementValue": value,
        "sensorType": sensorType,
        "year": d.getFullYear(),
        "month": d.getMonth(),
        "day": d.getDate(),
        "hour": d.getHours(),
        "minutes": d.getMinutes()
    };

    context.log(`Output content: ${output}`);

    context.bindings.outputDocument = output;

    context.done();
};