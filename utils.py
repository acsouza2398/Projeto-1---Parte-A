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
    with open(path, "rb") as file:
        data = file.read()
        return data   

def load_data():
    db = Database('bank')
    notes = db.get_all()
    return notes

def load_template(file_path):
    file = open(file_path, encoding='utf-8')
    content = file.read()
    file.close()
    return content

def add_notes(note):
    db = Database("bank")
    print("note", note)
    add = db.add(Note(title = note['title'], content = note['content']))

def delete_note(id):
    db = Database('bank')
    delete = db.delete(id)

def update_note(id, correct):
    db = Database('bank')
    if correct:
        update = db.update(Note(id = id, title = correct["title"], content = correct["content"]))
        print("see here", correct)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        return ("HTTP/1.1 " + str(code)+ " " + str(reason) + '\n' + str(headers) + '\n\n' + str(body)).encode()  
    else:
        return ("HTTP/1.1 " + str(code)+ " " + str(reason) + '\n\n' + str(body)).encode() 


