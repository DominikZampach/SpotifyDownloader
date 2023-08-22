from flask import Flask, request
import json, os, datetime

#This application is for getting query from website redirect
app = Flask("Get redirect query")

@app.route("/redirect", methods=["GET"])
def redirect(): #redirect url, where i will save args
    saved = request.args
    data = {"args": saved}
    json_object = json.dumps(data, indent=4)
    with open ("args.json", "w") as file:
        file.write(json_object)

    return "<h1>You can quit this site now</h1>"


print("Server is running")
#For now, i will let it be started by user (completed for now)
app.run(port=5678)