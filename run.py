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
        url="https://passport.bilibili.com/web/captcha/combine?plat=6"
    ).json()
    result = r.get("data", "").get("result", "")
    response = {
        "success": 1 if result else 0,
        "gt": result.get("gt", ""),
        "challenge": result.get("challenge", ""),
        "new_captcha": True
    }
    return json.dumps(response)

@app.route("/")
def login():
    return render_template("index.html")

if __name__ == "__main__":
    app.secret_key = "www"
    app.run()
