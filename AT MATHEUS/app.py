from flask import Flask, render_template, redirect, request
from classes.conta import Conta

app = Flask(__name__)


conta1 = Conta(33334, "Guilherme", 5000, 3000)
conta2 = Conta(33333, "Joao", 5000, 3000)
conta3 = Conta(33332, "Viktor", 5000, 3000)


contas = [conta1, conta2, conta3]

#Funções de roteamento e carregamento de páginas
@app.route('/cadastro')
def CarregarPaginaAdicionarConta():
    return render_template('adicionar.html')


@app.route('/listarcontas')
def CarregarPaginaListarContas():
    return render_template('listar.html',  lista_conta=contas)


@app.route('/')
def CarregarPaginaIndex():
    return render_template('index.html')


@app.route('/editar')
def CarregarPaginaEditar():
    index = int(request.args.get("index"))
    conta = contas[index]
    return render_template('editar.html', conta=conta, index=index)

#Funções de cadastro, edição e exclusão
@app.route('/contas/cadastar', methods=["GET"])
def cadastrado():
    nomeTitular = request.args.get('nomeTitular')
    numeroConta = request.args.get('numeroConta')
    saldo = int(request.args.get('saldo'))
    chequeEspecial = int(request.args.get('chequeEspecial'))

    novaConta = Conta(numeroConta, nomeTitular, saldo, chequeEspecial)
    contas.append(novaConta)
    return redirect('/listarcontas')


@app.route('/contas/editar')
def edicao():
    index = int(request.args.get("index"))
    conta = contas[index]
    conta.nomeTitular = request.args.get('nomeTitular')
    conta.numeroConta = request.args.get('numeroConta')
    conta.saldo = int(request.args.get('saldo'))
    conta.chequeEspecial = int(request.args.get('chequeEspecial'))
    return redirect('/listarcontas')


@app.route('/contas/excluir')
def excluir():
    index = int(request.args.get("index"))
    contas.pop(index)
    return redirect('/listarcontas')

if __name__ == "__main__":
    app.run(debug=True)
