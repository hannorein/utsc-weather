from functools import wraps
from flask import Flask, abort, render_template, send_from_directory, request, redirect, Response
import urllib2

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def page_main():
    current_conditions = urllib2.urlopen("http://weather.utsc.utoronto.ca/current_conditions.txt").read().split("\n")[6:17]

    return render_template("index.html",
        current_conditions = current_conditions,
        )

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
