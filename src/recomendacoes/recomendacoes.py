from pymongo import MongoClient

import os

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path=('/rpc')

MONGO_SERVER = os.environ['MONGO_SERVER']
PORT = int(os.environ['RECOMENDACOES_PORT'])

def get_database():
    client = MongoClient(MONGO_SERVER)
    return client['acervo']

def adicionar_livro(data):
    
    db = get_database()
    colection = db['livros']
    colection.insert_one(data)
    
    return "done"

def listar_livros():
    retorno = []
    
    db = get_database()
    colection = db['livros']

    for x in colection.find():
        retorno.append({'_id':str(x['_id']),'titulo':x['titulo'],'anoPublicacao':x['anoPublicacao'],'categoria':x['categoria']})

    return retorno

def listar_livros_categoria(categoria):
    retorno = []

    db = get_database()
    colection = db['livros']

    for x in colection.find({'categoria':categoria}):
        retorno.append({'_id':str(x['_id']),'titulo':x['titulo'],'anoPublicacao':x['anoPublicacao'],'categoria':x['categoria']})

    return retorno
    

if __name__ == '__main__':
    server = SimpleXMLRPCServer(('0.0.0.0',PORT))
    
    print("Listening...")

    server.register_function(adicionar_livro,"adicionar_livro")
    server.register_function(listar_livros,"listar_livros")
    server.register_function(listar_livros_categoria,"listar_livros_categoria")
    
    server.register_introspection_functions()
    server.serve_forever()
