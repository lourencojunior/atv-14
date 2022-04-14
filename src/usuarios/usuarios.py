from pymongo import MongoClient

import os

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_path=('/rpc')

MONGO_SERVER = os.environ['MONGO_SERVER']
PORT = int(os.environ['USUARIOS_PORT'])

def get_database():
    client = MongoClient(MONGO_SERVER)
    return client['acervo']

def adicionar_usuario(data):
    
    db = get_database()
    colection = db['usuarios']
    colection.insert_one(data)
    
    return "done"

def listar_usuarios():
    retorno = []
    
    db = get_database()
    colection = db['usuarios']

    for x in colection.find():
        retorno.append({'_id':str(x['_id']),'nome':x['nome'],'email':x['email']})

    return retorno


if __name__ == '__main__':
    server = SimpleXMLRPCServer(('0.0.0.0',PORT))
    
    print("Listening...")

    server.register_function(adicionar_usuario,"adicionar_usuario")
    server.register_function(listar_usuarios,"listar_usuarios")
    
    server.register_introspection_functions()
    server.serve_forever()
