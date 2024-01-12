from flask import Flask, render_template, jsonify , request
import os, sys


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('test.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)