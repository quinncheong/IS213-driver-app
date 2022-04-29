from urllib import response
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import hashlib
import json

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate('privateKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ninja-truck-9fb80-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Logins')

@app.route("/")
def hello():
    return 'Login connected'

@app.route("/create", methods=['GET'])
def create_password():
    password = 'root1'
    h = hashlib.new('sha256')
    h.update(password.encode('utf8'))
    return h.hexdigest()


@app.route("/authenticate", methods=['POST'])
def login():
    
    data = request.get_json()
    print(data)
    username = data['username']
    password = data['password']
    user_dict = ref.child(username).get()
    h = hashlib.new('sha256')
    h.update(password.encode('utf8'))
    hashed = h.hexdigest()
    if user_dict and user_dict['Password'] == hashed:
        return jsonify(
            {
                "code": 200,
                "data": user_dict['DriverID'],

            } 
        ), 200
    else:
        return jsonify(
            {
                "code": 401,
                "message": "Incorrect username and/or password"
            }
        ), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)