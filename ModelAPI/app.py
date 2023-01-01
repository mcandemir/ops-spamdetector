import os

from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()  # for local work
import requests

app = Flask(__name__)
modelapi_route = os.environ['MODELAPI_ROUTE']
modelapi_port = os.environ['MODELAPI_PORT']
modelapi_host = os.environ['MODELAPI_HOST']
seldon_endpoint = os.environ['SELDON_ENDPOINT']


@app.route("/detect", methods=['POST'])
def detect():
    # decode data
    text = request.data
    decoded_text = [bytes.decode(text)]

    # get prediction
    text1 = ['Hello, we have finally met. You have earned $3000 dollars. You have 1 hour to claim your prize. Start now!']
    text2 = ['Hello James, how are you? Can you please set a meeting at 9 pm? Thank you.']
    


    request = {"data":{"names":["text"],"tensor":{"shape":[1],"values":[decoded_text]}}}

    inference_request = {
        "parameters": {
            "content_type": "str"
        },
        "inputs": [
            {
            "name": "decoded_text",
            "data": decoded_text,
            "datatype": "BYTES",
            "shape": [1],
            },
        ]
    }
    
    # endpoint = "http://localhost:8080/v2/models/model/versions/v1.2.0/infer"
    response = requests.post(seldon_endpoint, json=request)
    json = response.json()
    return json


if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(modelapi_port),
        host=modelapi_host
    )
