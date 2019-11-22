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
        print(request.data)
        obj_body = json.loads(request.data)
        print(obj_body)
        msg_list = messages['messages']
        for item in msg_list:
            if item['id'] == id:
                item['id'] = obj_body['id']
                item['title'] = obj_body['title']
                return "updated!"
        return f'not found item with id -- {id}'
    if request.method == 'DELETE':
        msg_list = messages['messages']
        index = 0
        for index, item in enumerate(msg_list):
            if item['id'] == id:
                del msg_list[index]
                return 'deleted!'
        return f'not found item with id -- {id}'

messages = { 'messages' :
    [{'id' : 1, 'title' : 'Hello'},
    {'id' : 2, 'title' : 'How are you?'}] }

@app.route('/get1')
def get1():
    return render_template('pageget.html')

app.run(debug=True)
