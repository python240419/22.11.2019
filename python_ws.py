import requests # need to install in settings
import json

resp = requests.get\
    ("http://127.0.0.1:5000/messages")
print(f'Status code = {resp.status_code}')
#print(f'Header = {resp.headers}')
#print(resp.content)

d = json.loads(resp.content)
class Todos:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

t = Todos(d)
print(t.messages)
print(t.messages[0]['title'])

resp = requests.post\
    ("http://127.0.0.1:5000/messages",
     '{"id" : 5, "title" : "post5"}')
print(f'Status code = {resp.status_code}')
