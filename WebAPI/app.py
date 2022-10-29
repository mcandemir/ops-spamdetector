import os
import requests
from flask import Flask, render_template, request


app = Flask(__name__)
modelapi_service = os.environ['MODELAPI_SERVICE']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    mail = request.form['mail']
    r = requests.post(modelapi_service, data=mail)
    return render_template('index.html', mail=r.text)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0'
    )
