import json

import requests
from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    DEBUG=False,
)

@app.route("/bilibili/combine", methods=["GET"])
def get_pc_captcha():
    r = requests.get(
        url="https://www.geetest.com/demo/gt/register-slide"
    ).json()
    return json.dumps(r)

@app.route("/")
def login():
    return render_template("index.html")

if __name__ == "__main__":
    app.secret_key = "www"
    app.run()
