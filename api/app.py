from flask import Flask, jsonify, request
from flask_cors import CORS
from assistant import Assistant
from googleadap import GoogleWebHook
from dialog import fetch_dialog
from brain import fetch_model, fetch_know

app = Flask(__name__)
CORS(app)

assistant = Assistant()
googleWH = GoogleWebHook(assistant)

@app.route('/')
def hi():
    return 'Hi, am i David!'

@app.route('/train')
def train():
    assistant.train()
    return "OK"   

@app.route('/dialog', methods=['POST'])
def dialog():
    data = request.get_json()
    return jsonify(assistant.respond(data['input']))    
    
@app.route('/google', methods=['POST'])
def google():
    data = request.get_json()
    return jsonify(googleWH.handle(data))  

@app.route('/data/dialog')
def data_dialog():
    return jsonify(fetch_dialog())  

@app.route('/data/know')
def data_know():
    return jsonify(fetch_know())           

if __name__ == '__main__':
    app.run(host='0.0.0.0')