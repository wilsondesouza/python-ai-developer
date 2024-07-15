import textwrap
from abc import ABC, abstractmethod

class Conta(ABC):
    LIMITE_SAQUES = 3

    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class ContaCorrente(Conta):
    LIMITE = 500

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.LIMITE:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        if any(usuario.cpf == cpf for usuario in self.usuarios):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        self.usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = next((usuario for usuario in self.usuarios if usuario.cpf == cpf), None)

        if usuario:
            numero_conta = len(self.contas) + 1
            conta = ContaCorrente("0001", numero_conta, usuario)
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(f"Agência:\t{conta.agencia}\nC/C:\t\t{conta.numero_conta}\nTitular:\t{conta.usuario.nome}\n")

class Menu:
    @staticmethod
    def exibir():
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))

    @staticmethod
    def executar_opcao(banco):
        while True:
            opcao = Menu.exibir()

            if opcao == "d":
                numero_conta = int(input("Informe o número da conta: "))
                valor = float(input("Informe o valor do depósito: "))
                conta = next((conta for conta in banco.contas if conta.numero_conta == numero_conta), None)
                if conta:
                    conta.depositar(valor)
                else:
                    print("\n@@@ Conta não encontrada! @@@")

            elif opcao == "s":
                numero_conta = int(input("Informe o número da conta: "))
                valor = float(input("Informe o valor do saque: "))
                conta = next((conta for conta in banco.contas if conta.numero_conta == numero_conta), None)
                if conta:
                    conta.sacar(valor)
                else:
                    print("\n@@@ Conta não encontrada! @@@")

            elif opcao == "e":
                numero_conta = int(input("Informe o número da conta: "))
                conta = next((conta for conta in banco.contas if conta.numero_conta == numero_conta), None)
                if conta:
                    conta.exibir_extrato()
                else:
                    print("\n@@@ Conta não encontrada! @@@")

            elif opcao == "nu":
                banco.criar_usuario()

            elif opcao == "nc":
                banco.criar_conta()

            elif opcao == "lc":
                banco.listar_contas()

            elif opcao == "q":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

def main():
    banco = Banco()
    Menu.executar_opcao(banco)

if __name__ == "__main__":
    main()