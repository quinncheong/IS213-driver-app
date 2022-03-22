from flask import Flask, request, jsonify
from flask_cors import CORS
from invokes import invoke_http
from os import environ


app = Flask(__name__)
CORS(app)


customerURL = environ.get('customerURL')
# customerURL = 'http://localhost:5004/customer'


@app.route("/customer", methods=['POST'])
def getDeliveryAddress():

    data = request.get_json()
    customers={}
    for customerId in data:
        response = invoke_http(
            customerURL+"/"+customerId, method='GET',
        )
        customers[customerId]=response['data']


    customerList = []
    for k, v in customers.items():
        v["customerID"] = k
        customerList.append(v)
    return jsonify(
        {
            "code": 200,
            "data": customerList
        }
    ), 200


if __name__ == '__main__':
    # app.run(port=5010, debug=True)
    app.run(host='0.0.0.0', port=5010, debug=True)
