
const express = require("express");
const bodyParser = require("body-parser");
const router = require("./controller/routes");

const app = express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json({limit: "1024mb"}));

app.use(router);

const PORT = process.env.PORT || 5000;

app.listen(PORT, function(){
    console.log(`Running server on port ${PORT}`);
});