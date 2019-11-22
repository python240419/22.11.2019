from flask import Flask
from flask import render_template, request, redirect,url_for
import json

@app.route('/messages', methods=['GET', 'POST','PUT', 'DELETE'])
def webservice():
    messages = { 'messages' :
                       [{'id' : 1, 'title' : 'Hello'},
                         {'id' : 2, 'title' : 'How are you?'}] }
    #print(request.data)
    #d = json.loads(request.data)
    #print(d)
    if request.method == 'GET':
        return messages
    if request.method == 'POST':
        return 'You posted'
    if request.method == 'PUT':
        return 'You put -- update'
    if request.method == 'DELETE':
        return 'You deleted'
        
app.run(debug=True)
