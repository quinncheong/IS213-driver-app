from flask import Flask, request, jsonify
from flask_cors import CORS
from invokes import invoke_http
from os import environ

from send_message import send_message
from send_email import send_email

app = Flask(__name__)
CORS(app)


customerURL = environ.get('customerURL')
parcelURL = environ.get('parcelURL')

emails =  [
    "quinncheong.2019@scis.smu.edu.sg", 
    "ian.chia.2020@scis.smu.edu.sg", 
    "jsebastian.2020@scis.smu.edu.sg"
]

# customerURL = 'http://localhost:5004/customer'
# parcelURL = 'http://localhost:5003/parcel'

@app.route("/")
def healthcheck():
    return 'Update Parcel Status is up and running!'

@app.route("/test")
def test():

    email_body = f"""<h3>Hello Admin Team,</h3>
        <p>The Parcel with ID: {12345} for User: {12345678} has failed to deliver.</p>
		<p>Please look into this to resolve the parcel issue.</p>"""

    email_message = {
        "subject": f"Failed Delivery for Parcel: {12345}",
        "body": email_body,
        "emails": emails
    }
    send_email(email_message)

    return jsonify("OK", 200)

@app.route("/updateParcelStatus/<string:parcelId>", methods=['POST'])
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

    #send sms and destructure customer data
    customter_name = customer["CustomerName"]

    phone_number = f"+65{customer['PhoneNumber']}"

    if parcel['Status'] == 'Failed':
        msg_body = f"Hi {customter_name}, your parcel with ID {parcelId} has failed to deliver."

        email_body = f"""<h3>Hello Admin Team,</h3>
        <p>The Parcel with ID: {message.parcelId} for User: {message.customerName} has failed to deliver.</p>
		<p>Please look into this to resolve the parcel issue.</p>"""

        email_message = {
            "subject": f"Failed Delivery for Parcel: ${message.parcelId}",
            "body": email_body,
            "emails": emails
        }

        send_email(email_message)
    else:
        msg_body = f"Dear {customter_name}, your parcel with ID: {parcelId} has been delivered."

    message = {
        "phoneNumber": phone_number,
        "body": msg_body,
    }

    #msg_status can be True or False, depending on err.
    msg_status = send_message(message) 

    email_message = {
        "parcelId": parcelId,
        "customerName": customter_name,
    }
    send_email(email_message)
    
    return jsonify(
        {
            "code": 200,
            "data": parcel
        }
    ),200

# This test endpoint is to be used which will send a mock message to kafka topic
# @app.route('/test')
# def msg_test():
#     phone_number = "+6597248790";
#     customter_name = "Ian Chia";
#     msg_body = f"Dear {customter_name}, your parcel with id: {12345} has been delivered."

#     message = {
#         "phoneNumber": phone_number,
#         "body": msg_body,
#     }

#     #msg_status can be True or False, depending on err.
#     msg_status = send_message(message) 
#     return 'Gucci'


if __name__ == '__main__':
    # app.run(port=5020, debug=True)
    app.run(host='0.0.0.0', port=5020, debug=True)
