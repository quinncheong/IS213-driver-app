from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)
CORS(app)
# Fetch the service account key JSON file contents
cred = credentials.Certificate('../privateKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ninja-truck-9fb80-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('Parcels')

@app.route("/")
def hello():
    return 'Parcel connected'

@app.route("/parcel/<string:driverId>")
def getParcels(driverId):
    parcels = ref.order_by_child('DriverID').equal_to(driverId).get()
    return jsonify(
        {
            "code": 200,
            "data": parcels,
        }
    ), 200

@app.route("/parcel/<string:parcelId>", methods=['PUT'])
def setParcelStatus(parcelId):
    data = request.get_json()
    status = data['status']
    reason = data['reason']
    parcel = ref.child(parcelId)
    parcel.child('Status').set(status)
    parcel.child("Reason").set(reason)
    timeDelivered = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    parcel.child("TimeDelivered").set(timeDelivered)

    return jsonify(
        {
            "code": 200,
            "data": parcel.get()
        }
    ),200


if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(host='0.0.0.0', port=5003, debug=True)