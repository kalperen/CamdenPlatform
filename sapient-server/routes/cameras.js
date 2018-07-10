var express = require('express');
var router = express.Router();

var documentClient = require("documentdb").DocumentClient;

var endpoint = 'https://camdenhub-db.documents.azure.com:443/';
var primaryKey = 'n3SH7g3IJw3ppZAETBNjvfo7aiq5AdxtnABefhguqOst6XLmWgDGo0NyngSW4xnQ2xopAvg2BRfEiO5fE9s6sA==';
var client = new documentClient(endpoint, { "masterKey": primaryKey });

var databaseUrl = `dbs/CamdenHubDB`;
var collectionUrl = `${databaseUrl}/colls/Cameras`;

router.post('/addCamera', function(req, res) {
    res.setHeader('Content-Type', 'application/json');

    client.createDocument(collectionUrl, req.body, (err, result) => {
        if (err) console.log(' error: ' + err.toString());
        res.send(result);
        console.log(result);
    });
})

router.get('/getCameras', function(req, res) {
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

router.delete('/deleteCamera/:cameraId', function(req, res) {
    res.setHeader('Content-Type', 'application/json');

    console.log(req.params.cameraId);

    var query = "SELECT * FROM c WHERE c.cameraId = '" + req.params.cameraId + "'";

    var querySpec = {
        'query': query
    }

    client.queryDocuments(collectionUrl, querySpec).toArray(function(err, results) {
        if (err) console.log(' error: ' + err.toString());
        console.log(results);
        client.deleteDocument(collectionUrl + '/docs/' + results[0].id, function (err) {
            if (err) {
                console.log(' error: ' + err);
            } else {
                console.log('Document deleted');
            }
        });
    });
})

module.exports = router;