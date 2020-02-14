from flask import Flask

server = Flask(__name__)

from app.controller import *
