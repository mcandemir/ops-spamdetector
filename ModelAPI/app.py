import os
from dotenv import load_dotenv
load_dotenv()  # for local work
import numpy as np
from flask import Flask, request
import tensorflow as tf
import pickle
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

app = Flask(__name__)
modelapi_route = os.environ['MODELAPI_ROUTE']
modelapi_port = os.environ['MODELAPI_PORT']
modelapi_host = os.environ['MODELAPI_HOST']
model = tf.keras.models.load_model('spamdetector.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


@app.route("/detect", methods=['POST'])
def detect():
    mail = request.data
    decoded_mail = [bytes.decode(mail)]

    tokenized_text = tokenizer.texts_to_sequences(decoded_mail)
    pad_text = pad_sequences(tokenized_text, maxlen=162)
    p = model.predict(pad_text)

    if p[0][0] > 0.2:
        return "mail is a spam"
    else:
        return "mail is not a spam"


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(modelapi_port),
        host=modelapi_host
    )
