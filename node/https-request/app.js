const https = require('http');

const data = JSON.stringify({ todo: 'Buy the milk - song' })
https.globalAgent.options.secureProtocol = 'SSLv3_method';


// const dns = require('dns');
// dns.setDefaultResultOrder('ipv4first');
//require("http").get("http://localhost:3004/", res => console.log(res.statusCode))

const option = {
    host: '127.0.0.1',
    port: 8000,
    path: '/todos/',
    method: 'GET',
}

const req = https.request(option, res => {
    console.log(`statusCode : ${res.statusCode}`)
    res.on('data', d => {
        process.stdout.write(d);
    })
})

req.on('error', error => {
    console.log(error);
});

req.write(data);
req.end();