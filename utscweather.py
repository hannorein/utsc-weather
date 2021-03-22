from functools import wraps
from flask import Flask, abort, render_template, send_from_directory, request, redirect, Response
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def page_main():
    with urllib.request.urlopen("https://weather.utsc.utoronto.ca/data/current_conditions.txt") as response:
        rawdata = response.read().decode("ascii")
    rawdata = rawdata.replace("deg C","&#176;C")
    rawdata = rawdata.replace("deg","&#176;")
    rawdata = rawdata.replace("^2","&#178;")
    rawdata = rawdata.split("\n")[6:17]

    with urllib.request.urlopen("https://weather.utsc.utoronto.ca/data/Hourly_current_month.dat") as response:
        hourly = response.read().decode("ascii")
    hourly = hourly.split("\n")

    data = []

    mapper = {
        0:2,   #temp
        1:8,   #rel
        2:9,   #baro
        3:10,   #wind speed
        4:11,   #wind direction
        5:12,   #rain
        6:13,   #solar
        7:14,   #sky
        8:15,   #hum ind
        9:7,   #dew
        10:16,   #wind chill
    }
    for i,d in enumerate(rawdata):
        temp_array = []
        for h in hourly[-24*7:]:
            fields = h.strip().split(",")
            if len(fields)<16:
                continue
            temp_array.append({"date":fields[0].strip("\""), "value":float(fields[mapper[i]])})
        data.append([d,json.dumps(temp_array)])


    return render_template("index.html",
        current_conditions = data,
        temp_array = json.dumps(temp_array),
        )

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
