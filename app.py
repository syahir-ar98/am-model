import urllib.request
import io
import json
import os
import ssl
from flask import Flask, jsonify, request
from flask_cors import CORS

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

app = Flask(__name__)
cors = CORS(app)

input1 = "0.8"
input2 = "0.4"
input3 = "0.7"
input4 = "0.7"
input5 = "0.3"
input6 = "0.3"
input7 = "0.4"
input8 = "0.4"
input9 = "0.4"
input10 = "0.6"
input11 = "0.2"
input12 = "0.2"
input13 = "0.4"
input14 = "0.8"
input15 = "0.4"
input16 = "0.7"
input17 = "0.8"
input18 = "0.2"
input19 = "0.3"
input20 = "0.7"


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
                "WebServiceInput0":
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
                        "'concave points_worst'": input20,
                    },
                ],
            },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'http://20.197.78.22:80/api/v1/service/model/score'
        # Replace this with the API key for the web service
        api_key = 't6iGShxgd8VgVMYQY7VvOrOL2j55zDUJ' 
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

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
