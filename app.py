from flask import Flask, request
import json

#This application is for getting query from website redirect
app = Flask("Get redirect query")

global args

@app.route("/redirect", methods=["GET"])
def redirect(): #redirect url, where i will save args
    #Write args into json file with timestands
    return "<h1>You can quit this site now</h1>"

@app.route("/get_query", methods=["GET"])
def get_query(): #request for auth.py to get that args
    return args

print("Server is running")
app.run(port=5000)