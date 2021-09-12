import json
from database import *

def extract_route(requisicao):
    if requisicao.startswith("GET /"):
        start = requisicao.split("GET /")
    else:
        start = requisicao.split("POST /")

    endereco = start[1].split(" ")

    return endereco[0]

def read_file(path):
    #lista = str(path).split(".")
    #if lista[-1]=="txt" or lista[-1]=="html" or lista[-1]=="css" or lista[-1]=="js":
    #    with open(path, "rt", encoding='utf-8') as file:
    #        text = file.read()
    #        return text
    #else:
    #    with open(path, "rb") as file:
    #        binary = file.read()
    #    return binary
    with open(path, "rb") as file:
        data = file.read()
        return data   

def load_data():
    #filePath = "data/"+nomeJson
    #with open(filePath, "rt", encoding="utf-8") as text:
    #    content = text.read()
    #    contentPython = json.loads(content)
    #    return contentPython
    db = Database('bank')
    notes = db.get_all()
    return notes

def load_template(file_path):
    file = open(file_path, encoding='utf-8')
    content = file.read()
    file.close()
    return content

def add_notes(note):
    #loc = "data/notes.json"
    #with open(loc, "rt", encoding="UTF-8") as file:
    #    data = json.load(file)
    #    data.update(note)
    #    file.seek(0)
    #    d = json.dump(data, file)
    #   return d
    db = Database("bank")
    print("note", note)
    add = db.add(Note(title = note['title'], content = note['content']))

def delete(id):
    db = Database('bank')
    delete = db.delete(id)

def update(id, correct):
    db = Database('bank')
    update = db.update(Note(id = id, title = correct['title'], content = correct['content']))

    

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        return ("HTTP/1.1 " + str(code)+ " " + str(reason) + '\n' + str(headers) + '\n\n' + str(body)).encode()  
    else:
        return ("HTTP/1.1 " + str(code)+ " " + str(reason) + '\n\n' + str(body)).encode() 


