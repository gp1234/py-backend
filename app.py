from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from hash import get_signature


app = Flask(__name__)     
cors = CORS(app)

@app.route("/")           
def greeting():                    
    return "Basic Authentication server"

@app.route("/signature",methods=['POST', 'OPTIONS'])
def getSignature():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
            message = request.json
            message = message['message']
            response = get_signature(message)
            return response
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))



def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

    
if __name__ == "__main__":       
    app.run(debug=True)                