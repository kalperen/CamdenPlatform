var express = require('express');
var router = express.Router();

var documentClient = require("documentdb").DocumentClient;

var endpoint = 'https://camdenhub-db.documents.azure.com:443/';
var primaryKey = 'n3SH7g3IJw3ppZAETBNjvfo7aiq5AdxtnABefhguqOst6XLmWgDGo0NyngSW4xnQ2xopAvg2BRfEiO5fE9s6sA==';
var client = new documentClient(endpoint, { "masterKey": primaryKey });

var databaseUrl = `dbs/CamdenHubDB`;
var collectionUrl = `${databaseUrl}/colls/Telemetries`;

router.post('/getTelemetries', function(req, res) {
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

module.exports = router;