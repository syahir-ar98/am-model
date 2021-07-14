import urllib.request
import json
import io
import os
import ssl
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

input1 = "20.57"
input2 = "17.77"
input3 = "132.9"
input4 = "1326"
input5 = "0.07864"
input6 = "0.0869"
input7 = "0.07017"
input8 = "0.5435"
input9 = "3.398"
input10 = "74.08"
input11 = "0.01308"
input12 = "0.0186"
input13 = "0.0134"
input14 = "24.99"
input15 = "23.41"
input16 = "158.8"
input17 = "1956"
input18 = "0.1866"
input19 = "0.2416"
input20 = "0.186"


@app.route('/', methods=['GET', 'POST'])
def requestModel():
    global input1, input2, input3, input4, input5, input6, input7, input8, input9, input10
    global input11, input12, input13, input14, input15, input16, input17, input18, input19, input20

    if(request.method == "POST"):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        input1 = request_data['input1']
        input2 = request_data['input2']
        input3 = request_data['input3']
        input4 = request_data['input4']
        input5 = request_data['input5']
        input6 = request_data['input6']
        input7 = request_data['input7']
        input8 = request_data['input8']
        input9 = request_data['input9']
        input10 = request_data['input10']
        input11 = request_data['input11']
        input12 = request_data['input12']
        input13 = request_data['input13']
        input14 = request_data['input14']
        input15 = request_data['input15']
        input16 = request_data['input16']
        input17 = request_data['input17']
        input18 = request_data['input18']
        input19 = request_data['input19']
        input20 = request_data['input20']
        return "Hello World!"

    elif(request.method == "GET"):

        # Request data goes here
        data = {
            "Inputs": {
                "input1":
                [
                    {
                        'radius_mean': input1,
                        'texture_mean': input2,
                        'perimeter_mean': input3,
                        'area_mean': input4,
                        'compactness_mean': input5,
                        'concavity_mean': input6,
                        "'concave points_mean'": input7,
                        'radius_se': input8,
                        'perimeter_se': input9,
                        'area_se': input10,
                        'compactness_se': input11,
                        'concavity_se': input12,
                        "'concave points_se'": input13,
                        'radius_worst': input14,
                        'texture_worst': input15,
                        'perimeter_worst': input16,
                        'area_worst': input17,
                        'compactness_worst': input18,
                        'concavity_worst': input19,
                        'concave points_worst': input20,
                    }
                ],
            },
            "GlobalParameters":  {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/cdc3ed69ebd14c24a227cf0f2adee23c/services/fddbdaab586d4754888a48156af67ce3/execute?api-version=2.0&format=swagger'
        # Replace this with the API key for the web service
        api_key = 'BJYhnd2W+f/3JPPmOOZRYcPhucK2Kr4KRZilG68V1gOws7jK6+zsIGL+Kg+yVWVo8P48zC5AVrm6geQIJyysAA=='
        headers = {'Content-Type': 'application/json',
                   'Authorization': ('Bearer ' + api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            result = response.read()

            final_result = result.replace(b"'", b"'")
            my_json = json.load(io.BytesIO(final_result))
            print(my_json)
            return my_json
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8000)
