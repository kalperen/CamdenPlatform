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

var documentClient = require("documentdb").DocumentClient;

var endpoint = 'https://camdenhub-db.documents.azure.com:443/';
var primaryKey = 'n3SH7g3IJw3ppZAETBNjvfo7aiq5AdxtnABefhguqOst6XLmWgDGo0NyngSW4xnQ2xopAvg2BRfEiO5fE9s6sA==';
var client = new documentClient(endpoint, { "masterKey": primaryKey });

var databaseUrl = `dbs/CamdenHubDB`;
var collectionUrl = `${databaseUrl}/colls/Telemetries`;

app.post('/Telemetries', function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    var query = "SELECT * FROM c WHERE ";
    query += (req.body.deviceId != null) ? "c.deviceId = @deviceId AND " : "" ;
    query += (req.body.sensorType != null) ? "c.sensorType = @sensorType AND " : "" ;
    query += (req.body.measurementUnit != null) ? "c.measurementUnit = @measurementUnit AND " : "" ;
    query += (req.body.lowerBound != null) ? "c.measurementValue > " + req.body.lowerBound + " AND " : "";
    query += (req.body.upperBound != null) ? "c.measurementValue < " + req.body.upperBound + " AND " : "" ;
    query += (req.body.lowerBoundTime != null) ? "c['_ts'] > " + req.body.lowerBoundTime + " AND " : "";
    query += (req.body.upperBoundTime != null) ? "c['_ts'] < " + req.body.upperBoundTime + " AND " : "" ;
    query += "1 = 1";
    console.log(query);

    //TODO:
    //once it works, think about SQL injection
    var querySpec = {
        'query': query,

        "parameters": [
            { "name": "@deviceId", "value": req.body.deviceId },
            { "name": "@measurementUnit", "value": req.body.measurementUnit },
            { "name": "@sensorType", "value": req.body.sensorType },
        ]
    }

    client.queryDocuments(collectionUrl, querySpec).toArray(function(err, results) {
        
        if (err) console.log(' error: ' + err.toString());
        res.send(results);
        console.log(results);
    });
})
 
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

app.get('/devices', function (req, res) {
    registry.list((err, deviceList) => {
        if (err) console.log(' error: ' + err.toString());
        deviceList.forEach((device) => {
            let key = device.authentication ? device.authentication.symmetricKey.primaryKey : '<no primary key>';
            console.log(device.deviceId + ': ' + key);
        });
        res.send(deviceList);
    });
})

app.get('/device/:deviceId', function (req, res) {
    registry.get(req.params.deviceId, (err, device) => {
        if (!err){
            console.log(device);
            res.send(device);
        } else {
            console.log("error: " + err);
        }
        
    });
})

app.delete('/device/:deviceId', function (req, res) {
    registry.delete(req.params.deviceId, printAndContinue('delete'));
})

function printAndContinue(op, next) {
    return function printResult(err, deviceInfo, res) {
      if (err) console.log(op + ' error: ' + err.toString());
      if (res) console.log(op + ' status: ' + res.statusCode + ' ' + res.statusMessage);
      if (deviceInfo) console.log(op + ' device info: ' + JSON.stringify(deviceInfo));
      if (next) next();
    };
  }
 
app.listen(3000)