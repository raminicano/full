var axios = require('axios');
const env = require('dotenv').config({path:"../../.env"});
var data = JSON.stringify({
    "collection": "testdb",
    "database": "test",
    "dataSource": "Cluster0",
    "projection": {
    "_id" : 0
}});
            
var config = {
    method: 'post',
    url: 'https://data.mongodb-api.com/app/data-osxnp/endpoint/data/v1/action/findOne',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': process.env.ATLAS_API,
    },
    data: data
};
            
axios(config)
    .then(function (response) {
        console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
        console.log(error);
    });

