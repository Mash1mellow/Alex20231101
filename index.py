from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:黃植達 20231101<br>"
    X += "<a href=/db>課程網頁</a><br>"
    X += "<a href=/alex?nick=alex>個人介紹及系統時間</a><br>"
    X += "<a href=/account>表單傳值</a><br>"
    return X

@app.route("/db")
def db():
    return "<a href='https://drive.google.com/drive/folders/1JGHLQWpzT2QxSVPUwLxrIdYowijWy4h1'>海青班資料庫管理課程</a>"

@app.route("/alex", methods=["GET", "POST"])
def alex():
    now = str(datetime.now())
    user = request.values.get("nick")
    return render_template("alex.html", datetime=now, name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")


#if __name__ == "__main__":
    #app.run()
