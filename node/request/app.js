const express = require('express');
const request = require('request');
const CircularJSON = require('circular-json');
const app = express();

app.get('/', (req, res) => {
    res.send('Web Server Started~!!');
});

app.get('/hello', (req, res) => {
    res.send({ data: "Hello World" });
})

let option1 = "http://192.168.1.75:8000/hello"
app.get('/rhello', (req, res) => {
    request(option1, { json: true }, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        //res.send(body);
        res.send(CircularJSON.stringify(body));
    });
})

const data = JSON.stringify({ todo: 'Buy the milk - song' })
app.get("/data", function (req, res) {
    res.send(data);
});

let option2 = 'http://192.168.1.75:8000/data';
app.get('/rdata', (req, res) => {
    request(option2, { json: true }, (err, result, body) => {
        if (err) {
            return console.log(err);
        }
        res.send(CircularJSON.stringify(body));
    });
});

app.listen(8000, function () {
    console.log('8000 Port : Server Started ~!!')
});