var express = require('express'),
    bodyParser = require('body-parser'),
    path = require("path");

var deviceRouter = require('./routes/devices');
var telemetriesRouter = require('./routes/telemetries');
 
var app = express()

//support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

//tell express that www is the root of our public web folder
app.use(express.static(path.join(__dirname, 'www')));

//add headers to allow Cross-Origin Resource Sharing
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.use('/devices', deviceRouter);
app.use('/telemetries', telemetriesRouter);
 
app.listen(3000)