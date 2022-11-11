from flask import make_response, Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app,resources={
    r"/*":{
        "origins":"*"
    }
})

users = []
@app.route('/users', methods=['GET'])
def getUsers():
    res = make_response({"payload": users}, 200)
    res.headers['Access-Control-Allow-Origin']= "*"
    return res

@app.route('/users', methods=['POST'])
def createUser():
    newUser = request.get_json()
    users.append(newUser)
    res = make_response({"payload":users}, 201)
    res.headers['Access-Control-Allow-Origin']= "*"
    return res

app.run(port=8080,host='localhost',debug=True)