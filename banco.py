# Aqui farei algumas funcionalidades pertencentes ao mecanismo de um caixa eletrônico
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from pathlib import Path
import time
console = Console()
pasta_projeto = Path(__file__).parent
caminho_senha = pasta_projeto / 'senha.txt'

class CaixaEletronico:
    caixa = 1000

    def __init__(self, saldo):
        self.saldo = saldo

    def mostrar_menu(self):
        texto = """ Escolha o que deseja: 

1 - Consultar Saldo
2 - Sacar
3 - Depositar
4 - Alterar senha
5 - Sair
        """
        console.print(Panel.fit(texto, title="Menu", border_style="green"))

    def pedir_senha(self):
    # Essa funcionalidade será executada sempre no inicio do programa
    # A primeira vez pedirá uma "Nova Senha"
        password = input('Digite sua senha: ')

        with open(caminho_senha, 'r') as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == '':
                with open(caminho_senha, 'a') as arquivo:
                    arquivo.write(password)
                print('\033[32mSenha criada com sucesso\033[m')
            else:
                if password == conteudo:
                    pass
                else:
                    tentativa = 0
                    while password != conteudo:
                        tentativa += 1
                        print(f'\033[31mTentativa {tentativa} de 3\033[m')
                        password = input('\033[31mSenha incorreta! Tente novamente: \033[m')
                        if tentativa == 2:
                            print('\033[31mAcesso bloqueado\033[m')
                            exit()
   

    def consultar_saldo(self):
        texto_saldo = f'Seu saldo atual é: {self.saldo}'
        console.print(Panel.fit(texto_saldo))


    def deposito(self, dinheiro):
    # Aqui será executado o saque, dependendo da quantidade de dinheiro no caixa
        self.saldo += dinheiro

    def sacar(self, dinheiro):
    # Aqui o depósito é ilimitado, dependendo do dinheiro do usuário
        if (self.saldo - dinheiro) >= 0:
            self.saldo -= dinheiro
        else:
            print('\033[31mO saque não pode ser efetuado\033[m')

    def alterar_senha(self, password):
        with open(caminho_senha, "w") as arquivo:
            arquivo.write(password)
  




console.print(Panel("Seja Bem-Vindo ao Banco Python", style="green"))

caixa_eletronico = CaixaEletronico(CaixaEletronico.caixa)
caixa_eletronico.pedir_senha()

for i in track(range(10), description="Processando..."):
    time.sleep(0.25)

while True:
    caixa_eletronico.mostrar_menu()
    escolha = int(input('Sua opção: '))
    if escolha == 1:
        caixa_eletronico.consultar_saldo()
    elif escolha == 2:
        valor_saque = int(input('Quantos deseja sacar: '))
        caixa_eletronico.sacar(valor_saque)
    elif escolha == 3:
        valor_deposito = int(input('Quantos deseja depositar: '))
        caixa_eletronico.deposito(valor_deposito)
    elif escolha == 4:
        troca_de_senha = input('Nova senha: ')
        caixa_eletronico.alterar_senha(troca_de_senha)
    elif escolha == 5:
        break
    else:
        break
print('\033[33mVolte sempre!\033[m')
