from flask import Flask, render_template, redirect, request
from classes.conta import Conta

app = Flask(__name__)


conta1 = Conta(33334, "Guilherme Rodrigues Oliveira", 5000, 3000)
conta2 = Conta(33333, "João Amorim", 5000, 3000)
conta3 = Conta(33332, "Viktor da Silva", 5000, 3000)


lista_conta = [conta1, conta2, conta3]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
    return render_template('listar.html', lista_conta=lista_conta)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/adicionar/adicionado', method=["GET"])
def adicionar():
    nomeTitular = request.form.get('nomeTitular')
    numeroConta = request.form.get('numeroConta')
    saldo = request.form.get('saldo')
    chequeEspecial = request.form.get('chequeEspecial')

    novaConta = Conta(numeroConta, nomeTitular, saldo, chequeEspecial)
    lista_conta.append(novaConta)
    return redirect('/listar')

app.run()
