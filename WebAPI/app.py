import requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    mail = request.form['mail']
    r = requests.post("http://spamdetector-modelapi-service:5001/detect", data=mail)
    return render_template('index.html', mail=r.text)


# @app.route('/', methods=['GET'])
# def index_get():
#     prediction = requests.get("http://172.17.0.3:5001")
#     return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000,
    )
