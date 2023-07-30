MENU = """
--------------------------------------------------------------
Selecione uma operação a ser realizada:

[d] Depositar
[s] Sacar
[e] Saldo/Extrato
[q] Sair
=> """

class Conta:
    LIMITE_VALOR_SAQUE = 500
    LIMITE_QUANTIDADE_SAQUES = 3

    def __init__(self):
        self.saldo = 0
        self.extrato = ""
        self.quantidade_saques = 0

    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        self.adicionar_operacao_extrato(f"Deposito realizado no valor de R$ {valor:.2f}")
        return True

    def sacar(self, valor):
        if valor <= self.LIMITE_VALOR_SAQUE:
            if valor <= self.saldo and self.quantidade_saques < self.LIMITE_QUANTIDADE_SAQUES:
                self.saldo -= valor
                self.adicionar_operacao_extrato(f"Saque realizado no valor de R$ {valor:.2f}")
                self.quantidade_saques = self.quantidade_saques + 1
                return True
            else:
                print("Não existe saldo o suficiente para realizar o saque ou você ultrapassou a quantidade de saques no dia")
                return False
        else:
            print("O valor solicitado excede o limite de saque de R$ 500")
            return False

    def adicionar_operacao_extrato(self, detalhes):
        self.extrato = self.extrato + "\n" + detalhes

    def exibir_saldo_extrato(self):
        print("--------------------------------------------------------------")
        print(f"\nSaldo atual de R$ {self.saldo:.2f}")
        print("Este é o seu extrato: ")
        print(self.extrato)
    

conta = Conta()

while True:
    opcao = input(MENU)

    match opcao:
        case 'd':
            valor = float(input("Informe o valor a ser depositado na conta: "))
            conta.depositar(valor)

        case "s":
            valor = float(input("Informe o valor para sacar da conta (LIMITE DE R$ 500): "))
            conta.sacar(valor)
    
        case "e":
            conta.exibir_saldo_extrato()
    
        case "q":
            break