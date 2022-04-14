import xmlrpc.client


if __name__ == '__main__':

    client = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")
    
    #client.adicionar_livro({"titulo":"abc","anoPublicacao":2022,"categoria":1})
    
    ret = client.listar_livros_categoria(2)
    for r in ret:
        print(r)