var express = require('express');
var router = express.Router();

var documentClient = require("documentdb").DocumentClient;

var endpoint = 'https://camdenhub-db.documents.azure.com:443/';
var primaryKey = 'n3SH7g3IJw3ppZAETBNjvfo7aiq5AdxtnABefhguqOst6XLmWgDGo0NyngSW4xnQ2xopAvg2BRfEiO5fE9s6sA==';
var client = new documentClient(endpoint, { "masterKey": primaryKey });

var databaseUrl = `dbs/CamdenHubDB`;
var collectionUrl = `${databaseUrl}/colls/Classifications`;

router.post('/addClassification', function(req, res) {
    res.setHeader('Content-Type', 'application/json');

    client.createDocument(collectionUrl, req.body, (err, result) => {
        if (err) console.log(' error: ' + err.toString());
        res.send(result);
        console.log(result);
    });
})

router.post('/getClassifications', function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    var query = "SELECT * FROM c WHERE ";
    query += (req.body.cameraId != null) ? "c.cameraId = @cameraId AND " : "" ;
    query += (req.body.lowerBoundTime != null) ? "c['_ts'] > " + req.body.lowerBoundTime + " AND " : "";
    query += (req.body.upperBoundTime != null) ? "c['_ts'] < " + req.body.upperBoundTime + " AND " : "" ;
    query += "1 = 1";

    //TODO:
    //once it works, think about SQL injection
    var querySpec = {
        'query': query,

        "parameters": [
            { "name": "@cameraId", "value": req.body.cameraId }
        ]
    }

    client.queryDocuments(collectionUrl, querySpec).toArray(function(err, results) {
        
        if (err) console.log(' error: ' + err.toString());
        res.send(results);
        console.log(results);
    });
})

module.exports = router;