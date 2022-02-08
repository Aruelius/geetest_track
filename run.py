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
        url="https://account.ch.com/default/initValidate?t=643"
    ).json()
    return r

@app.route("/")
def login():
    return render_template("index.html")

if __name__ == "__main__":
    app.secret_key = "www"
    app.run()
