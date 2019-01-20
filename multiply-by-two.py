from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/<int:id>')
def multiply_by_2(id):
    response = {}
    response["input"]=id
    response["multipliedby"] = 2
    response["result"] = id *2
    return jsonify(response)
