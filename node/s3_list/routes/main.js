const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const env = require('dotenv').config({path: '../../.env'});


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))


const AWS = require('aws-sdk')
const ID = process.env.ID
const SECRET = process.env.SECRET
const BUCKET_NAME = 'kibwa05'
const MYREGION = 'ap-northeast-2'
const s3 = new AWS.S3({ accessKeyId: ID, secretAccessKey: SECRET, region: MYREGION});

app.get('/list', (req, res) => {
    var params = {
        Bucket: BUCKET_NAME,
        Delimiter: '/',
        Prefix: 'uploadedFiles/'
    };
    s3.listObjects(params, function(err, data) {
        if (err) throw err;
        //res.json(data.Contents);
        res.writeHead(200)
        var template = `
            <!doctype html>
            <html>
            <head>
                <title>Result</title>
                <meta charset="utf-8">
            </head>
            <body>
                <table 

        `
    });
});

module.exports = app;