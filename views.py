from os import error, replace
from utils import load_data, load_template, add_notes, build_response, delete_note, update_note
import urllib

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus

        #titulo=Sorvete+de+banana 
        #detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("titulo"):
                params["title"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["content"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")

        add_notes(params)
        return build_response(code=303, reason='See Other', headers='Location: /')


    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('templates/components/note.html')
    notes_li = [
        note_template.format(id= note.id, title= note.title, content=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)
    return build_response(load_template('templates/index.html').format(notes=notes))

def  delete(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]

        id = urllib.parse.unquote_plus(corpo[corpo.find("=")+1:], encoding="utf-8", errors="replace")

        delete_note(int(id))

        return build_response(code=303, reason='See Other', headers='Location: /')


    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('templates/components/note.html')
    notes_li = [
        note_template.format(id= note.id, title= note.title, content=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)
    return build_response(load_template('templates/index.html').format(notes=notes))
    
def edit(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        id = urllib.parse.unquote_plus(corpo[corpo.find("=")+1:], encoding="utf-8", errors="replace")
        id_int = int(id.split('&')[0])
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("title"):
                params["title"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("content"):
                params["content"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
    
        update_note(id_int, params)

        return build_response(code=303, reason='See Other', headers='Location: /')
    
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('templates/components/note.html')
    notes_li = [
        note_template.format(id= note.id, title= note.title, content=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)
    return build_response(load_template('templates/index.html').format(notes=notes))
