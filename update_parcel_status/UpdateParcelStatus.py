from flask import Flask, request, jsonify
from flask_cors import CORS
from invokes import invoke_http
from os import environ


app = Flask(__name__)
CORS(app)


customerURL = environ.get('customerURL')
parcelURL = environ.get('parcelURL')

# customerURL = 'http://localhost:5004/customer'
# parcelURL = 'http://localhost:5003/parcel'


@app.route("/parcel/<string:parcelId>", methods=['POST'])
def updateParcelStatus(parcelId):

    response = invoke_http(
        parcelURL+'/'+parcelId, method='PUT',
        json=request.get_json()
    )
    parcel = response['data']

    response = invoke_http(
        customerURL+'/'+parcel['CustomerID'], method='GET',
        json=request.get_json()
    )
    customer = response['data']
    #send sms
    
    return jsonify(
        {
            "code": 200,
            "data": parcel
        }
    ),200


if __name__ == '__main__':
    # app.run(port=5020, debug=True)
    app.run(host='0.0.0.0', port=5020, debug=True)
