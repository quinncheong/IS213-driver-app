from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)
CORS(app)

# Fetch the service account key JSON file contents
cred = credentials.Certificate('privateKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ninja-truck-9fb80-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('Customers')

 
@app.route("/customer/<string:customerId>")
def getCustomer(customerId):

    customer = ref.child(customerId).get()
    return jsonify(
        {
            "code": 200,
            "data": customer
        }
    ), 200


if __name__ == '__main__':
    app.run(port=5004, debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=True)
