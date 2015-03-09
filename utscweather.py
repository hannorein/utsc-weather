from functools import wraps
from flask import Flask, abort, render_template, send_from_directory, request, redirect, Response
import urllib2
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def page_main():
    rawdata = urllib2.urlopen("http://weather.utsc.utoronto.ca/current_conditions.txt").read()
    rawdata = rawdata.replace("deg C","&#176;C")
    rawdata = rawdata.replace("deg","&#176;")
    rawdata = rawdata.replace("^2","&#178;")
    rawdata = rawdata.split("\n")[6:17]

    hourly = urllib2.urlopen("http://weather.utsc.utoronto.ca/Hourly_current_month.dat").read().strip().split("\n")[4:]
    
    data = []

    mapper = {
        0:2,   #temp
        1:3,   #rel
        2:5,   #baro
        3:7,   #wind speed
        4:8,   #wind direction
        5:6,   #rain
        6:9,   #solar
        7:10,   #sky
        8:11,   #hum ind
        9:4,   #dew
        10:12,   #wind chill
    }
    for i,d in enumerate(rawdata):
        temp_array = []
        for h in hourly[-24*7:]:
            fields = h.split(",")
            temp_array.append({"date":fields[0].strip("\""), "value":float(fields[mapper[i]])})
        data.append([d,json.dumps(temp_array)])

     

    return render_template("index.html",
        current_conditions = data,
        temp_array = json.dumps(temp_array),
        )

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
