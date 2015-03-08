from functools import wraps
from flask import Flask, abort, render_template, send_from_directory, request, redirect, Response
import urllib2

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def page_main():
    rawdata = urllib2.urlopen("http://weather.utsc.utoronto.ca/current_conditions.txt").read()
    rawdata = rawdata.replace("deg C","&#176;C")
    rawdata = rawdata.replace("deg","&#176;")
    rawdata = rawdata.replace("^2","&#178;")
    
    rawdata = rawdata.split("\n")[6:17]
    

    return render_template("index.html",
        current_conditions = rawdata,
        )

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
