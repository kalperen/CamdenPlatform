var express = require('express'),
    bodyParser = require('body-parser'),
    path = require("path");
 
var app = express()

//support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

//tell express that www is the root of our public web folder
app.use(express.static(path.join(__dirname, 'www')));

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

var iothub = require('azure-iothub');
 
var connectionString = 'HostName=CamdenHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=SFHea3BfOt5IXppq69PmqWt7UmoHiSPN8TkiC/CEvPg=';
 
var registry = iothub.Registry.fromConnectionString(connectionString);

var device = {
    deviceId: null
    };
 
app.post('/addDevice', function(req, res) {
    res.setHeader('Content-Type', 'application/json');

    device.deviceId = req.body.deviceId;

    registry.create(device, function(err, deviceInfo, res1) {
        if (err) console.log(' error: ' + err.toString());
        if (res1) console.log(' status: ' + res1.statusCode + ' ' + res1.statusMessage);
        if (deviceInfo) console.log(' device info: ' + JSON.stringify(deviceInfo));
        res.send(deviceInfo);
    });
})
 
app.listen(3000)