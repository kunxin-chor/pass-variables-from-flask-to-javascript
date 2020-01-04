from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    pi= 3.14
    gst = 0.07
    return render_template('index.template.html', pi=pi, gst=gst)




# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)