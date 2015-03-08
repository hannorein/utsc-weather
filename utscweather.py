from functools import wraps
from flask import Flask, abort, render_template, send_from_directory, request, redirect, Response

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def page_main():
    return render_template("index.html",
        )

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
