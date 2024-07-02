from flask import Flask, render_template, redirect, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def homePage():
    dateAndTime = datetime.now()
    return render_template("home.html", dateAndTime = dateAndTime)

if __name__ == "__main__":
    app.run()