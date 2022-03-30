from flask import Flask, request, jsonify
from flask_cors import CORS
from invokes import invoke_http
from os import environ


app = Flask(__name__)
CORS(app)

loginURL = environ.get('loginURL')
driverURL = environ.get('driverURL')
parcelURL = environ.get('parcelURL')

# loginURL = 'http://localhost:5001/authenticate'
# driverURL = 'http://localhost:5002/driver'
# parcelURL = 'http://localhost:5003/parcel'


@app.route("/loadDashboard", methods=['POST'])
def loadDashboard():
    response= invoke_http(
        loginURL, method='POST',
        json=request.get_json()
    )

    if response['code'] != 200:
        return  response,response['code']
    driverId= response['data']


    response = invoke_http(
        driverURL+'/'+driverId, method='GET',
    )
    driver = response['data']

    response = invoke_http(
        parcelURL+'/'+driverId, method='GET',
    )
    parcels = response['data']

    parcelList = []
    for k, v in parcels.items():
        v["parcelID"] = k
        parcelList.append(v)

    return jsonify(
        {
            "code": 200,
            "data": {
                "driverId":driverId,
                "driver": driver,
                "parcels": parcelList,
            },
        }
    ), 200


if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
