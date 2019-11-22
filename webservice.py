from flask import Flask
from flask import render_template, request, redirect,url_for
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    return f'<html><h1><b>Welcome to Flask!</b></h1></html>'

@app.route('/messages', methods=['GET', 'PUT'])
def webservice():
    global messages
    if request.method == 'GET':
        return messages
    if request.method == 'POST':
        print(request.data)
        d = json.loads(request.data)
        print(d)
        messages['messages'].append(d)
        return 'You posted'

@app.route('/messages/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def webservicewithid(id):
    global messages
    if request.method == 'GET':
        msg_list = messages['messages']
        for item in msg_list:
            if item['id'] == id:
                return item
        return f'not found item with id -- {id}'
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
