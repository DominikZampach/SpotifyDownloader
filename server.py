from flask import Flask, request
import json

# This application is for getting query from website redirect
app = Flask("Get redirect query")


@app.route("/redirect", methods=["GET"])
def redirect():  # redirect url, where i will save args
    saved = request.args
    json_object = json.dumps(saved, indent=4)
    with open("data.json", "w") as file:
        file.write(json_object)

    return "<h1>You can quit this site now</h1>"


print("Server is running")
print("Just let this run on background, don't mind it at all.")
app.run(port=5678)

# EduLint done
# mypy
