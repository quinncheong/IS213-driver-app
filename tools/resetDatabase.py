import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./tools/privateKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ninja-truck-9fb80-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference()

def main():
    with open('./tools/database.json') as file:
        Json=json.load(file)
    return ref.set(Json)

print(main())
