var express = require('express');
var router = express.Router();

var documentClient = require("documentdb").DocumentClient;

var endpoint = 'https://camdenhub-db.documents.azure.com:443/';
var primaryKey = 'n3SH7g3IJw3ppZAETBNjvfo7aiq5AdxtnABefhguqOst6XLmWgDGo0NyngSW4xnQ2xopAvg2BRfEiO5fE9s6sA==';
var client = new documentClient(endpoint, { "masterKey": primaryKey });

var databaseUrl = `dbs/CamdenHubDB`;
var collectionUrl = `${databaseUrl}/colls/SensorTypes`;

router.get('/sensorTypes', function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    var query = "SELECT * FROM c";

    var querySpec = {
        'query': query
    }

    client.queryDocuments(collectionUrl, querySpec).toArray(function(err, results) {
        
        if (err) console.log(' error: ' + err.toString());
        res.send(results);
        console.log(results);
    });
})

router.get('/sensorType/:sensorId', function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    var query = "SELECT * FROM c WHERE c.sensorId = '" + req.params.sensorId + "'";

    var querySpec = {
        'query': query
    }
    client.queryDocuments(collectionUrl, querySpec).toArray(function(err, results) {
        
        if (err) console.log(' error: ' + err.toString());
        res.send(results[0]);
        console.log(results);
    });
})

router.post('/sensorType', function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    var sensorType = {
        sensorType : req.body.sensorType,
        sensorId : req.body.sensorId
    };

    client.createDocument(collectionUrl, sensorType, function(err, results) {
        if (err) console.log(' error: ' + err.toString());
        res.send(results);
        console.log(results);
    });
})

module.exports = router;