class Conta:
    LIMITE_VALOR_SAQUE = 500
    LIMITE_QUANTIDADE_SAQUES = 3

    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
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

class Banco:
    MENU = """
--------------------------------------------------------------
Selecione uma operação a ser realizada:

[d] Depositar
[s] Sacar
[e] Saldo/Extrato
[q] Sair
=> """

    def __init__(self):
        self.contas = list()
    
    def adicionar_conta(self):
        nome = input("Informe o nome do titular: ")
        self.contas.append(Conta(nome))
        print("Conta cadastrada com sucesso com número => " + str(len(self.contas)-1))

    def listar_contas(self):
        print("[Número da conta]: Nome do Titular")
        for index, conta in enumerate(self.contas):
            print(f"[{index}]: {conta.nome_titular}")
    
    def movimentar_conta(self):
        numero_conta = int(input("Informe o numero da conta: "))
        conta_atual = self.contas[numero_conta]
        while True:
            opcao = input(self.MENU)

            match opcao:
                case 'd':
                    valor = float(input("Informe o valor a ser depositado na conta: "))
                    conta_atual.depositar(valor)

                case "s":
                    valor = float(input("Informe o valor para sacar da conta (LIMITE DE R$ 500): "))
                    conta_atual.sacar(valor)

                case "e":
                    conta_atual.exibir_saldo_extrato()

                case "q":
                    break

banco = Banco()

MENU_BANCO = """
--------------------------------------------------------------
Selecione uma operação a ser realizada:

[c] Cadastrar uma conta
[l] Listar contas
[m] Movimentar conta
[q] Sair
=> """

while True:
           opcao = input(MENU_BANCO)
           match opcao:
               case 'c':
                   banco.adicionar_conta()
               case "l":
                   banco.listar_contas()
               case "m":
                   banco.movimentar_conta()
               case "q":
                   break