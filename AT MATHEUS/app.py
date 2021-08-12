from flask import Flask, render_template, redirect, request
from conta import Conta

app = Flask(__name__)


conta1 = Conta(33334, "Guilherme", 5000, 3000)
conta2 = Conta(33333, "Joao", 5000, 3000)
conta3 = Conta(33332, "Viktor", 5000, 3000)


contas = [conta1, conta2, conta3]


@app.route('/conta/cadastro')
def adicionar():
    return render_template('adicionar.html')


@app.route('/listarcontas')
def listarContas():
    return render_template('listar.html',  lista_conta=contas)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/conta/cadastar', methods=["GET"])
def cadastrado():
    nomeTitular = request.args.get('nomeTitular')
    numeroConta = request.args.get('numeroConta')
    saldo = int(request.args.get('saldo'))
    chequeEspecial = int(request.args.get('chequeEspecial'))

    novaConta = Conta(numeroConta, nomeTitular, saldo, chequeEspecial)
    contas.append(novaConta)
    return redirect('/')



app.run()
