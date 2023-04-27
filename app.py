from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/login/get", methods=['GET'])
def loginGet():
    id = request.args.get("id")
    passwd = request.args.get("password")

    print("id", id)
    print("password", passwd)

    if(id == "stephan" and passwd == "1234"):
        response = {
            "result": "success",
            "name": "Jongnam Won"
        }
    else:
        response = {
            "result": "fail"
        }

    return jsonify(response)


@app.route("/login/post", methods=['POST'])
def loginPost():
    params = request.get_json()
    print("request body ", params)

    if(params.get('id') == "stephan" and params.get('password') == "1234"):
        response = {
            "result": "success",
            "name": "Jongnam Won"
        }
    else:
        response = {
            "result": "fail"
        }

    return jsonify(response)