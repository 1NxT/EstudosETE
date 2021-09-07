class Conta:
    def __init__(self, numeroConta, nomeTitular, saldo, chequeEspecial):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        self.chequeEspecial = chequeEspecial
        self.saldoTotal = self.saldo + self.chequeEspecial



