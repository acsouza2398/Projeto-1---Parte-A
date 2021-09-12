import sqlite3
from dataclasses import dataclass

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database():
    def __init__(self,banco):
        name = banco+'.db'
        self.conn = sqlite3.connect(name)
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content TEXT NOT NULL);")

    def add(self, note):
        infos = ((note.id), (note.title), (note.content))
        command = "INSERT INTO note (id, title, content) VALUES (?,?,?)"
        self.conn.execute(command,infos)
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        list = []
        for linha in cursor:
           id = linha[0]
           title = linha[1]
           content = linha[2]
           list.append(Note(id = id, title = title, content = content))
        return list

    def update(self, entry):
        self.conn.execute(f"UPDATE note SET title='{entry.title}', content='{entry.content}' WHERE id={entry.id}")
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()