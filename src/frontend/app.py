
from flask import Flask
from flask import render_template
from flask import request   
import xmlrpc.client
import os
import sys

ACERVO_URL=os.environ['ACERVO_URL']
USUARIOS_URL=os.environ['USUARIOS_URL']
RECOMENDACOES_URL=os.environ['RECOMENDACOES_URL']




app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/acervo",methods=['GET', 'POST'])
def acervo():
    print(f"ACERVO=>{ACERVO_URL}", file=sys.stderr)
    client = xmlrpc.client.ServerProxy(ACERVO_URL)
    if request.method == 'POST':
        dados = request.form.to_dict()
        client.adicionar_livro(dados)
    ret = client.listar_livros()
    return render_template('acervo.html',livros=ret)

@app.route("/usuarios",methods=['GET', 'POST'])
def usuarios():
    print(f"USUARIOS=>{USUARIOS_URL}", file=sys.stderr)
    client = xmlrpc.client.ServerProxy(USUARIOS_URL)
    if request.method == 'POST':
        dados = request.form.to_dict()
        client.adicionar_usuario(dados)
    ret = client.listar_usuarios()
    return render_template('usuarios.html',usuarios=ret)

@app.route("/recomendacoes",methods=['GET'])
def recomendacoes():
    print(f"RECOMENDACOES=>{RECOMENDACOES_URL}", file=sys.stderr)
    client = xmlrpc.client.ServerProxy(RECOMENDACOES_URL)
    ret = client.listar_livros()
    return render_template('recomendacoes.html',livros=ret)