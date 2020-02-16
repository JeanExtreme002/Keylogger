
const express = require("express");
const bodyParser = require("body-parser");
const router = require("./controller/routes");

const app = express();

// Define configurações
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json({limit: "1024mb"}));

// Define as rotas
app.use(router);


// Executa o servidor

const PORT = process.env.PORT || 5000;

app.listen(PORT, function(){
    console.log(`Running server on port ${PORT}`);
});