import xmlrpc.client
import json

if __name__ == '__main__':

    client = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")
    

    entrada = input('Digite os dados do usuario {"nome":??,"email":??}:')

    client.adicionar_usuario(json.loads(entrada))
    
    ret = client.listar_usuarios()
    for r in ret:
        print(r)