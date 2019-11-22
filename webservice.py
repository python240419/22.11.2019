from flask import Flask
from flask import render_template, request, redirect,url_for
import json

app = Flask(__name__)


@app.route('/')
def home_page():
    return f'<html><h1><b>Welcome to Flask!</b></h1></html>'


@app.route('/messages', methods=['GET', 'POST','PUT', 'DELETE'])
def webservice():
    global messages
    if request.method == 'GET':
        return messages
    if request.method == 'POST':
        print(request.data)
        d = json.loads(request.data)
        print(d)
        # todo - add the d item to messages
        return 'You posted'
    if request.method == 'PUT':
        # todo - the same but update
        return 'You put -- update'
    if request.method == 'DELETE':
        # todo - delete
        return 'You deleted'
    
messages = { 'messages' :
    [{'id' : 1, 'title' : 'Hello'},
    {'id' : 2, 'title' : 'How are you?'}] }
        
app.run(debug=True)
