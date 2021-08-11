from flask import Flask, render_template, redirect, request
from classes.conta import Conta


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
    return render_template('listar.html')

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/adicionar/adicionado')
def adicionar():
    return redirect('/')

app.run()
