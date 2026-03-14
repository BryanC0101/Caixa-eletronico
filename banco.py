# Aqui farei algumas funcionalidades pertencentes ao mecanismo de um caixa eletrônico
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
import time


class CaixaEletronico:
    senha = []
    def mostrar_menu(self):
        texto = """ Escolha o que deseja: 

1 - Consultar Saldo
2 - Sacar
3 - Depositar
4 - Alterar senha
5 - Sair
        """
        console.print(Panel.fit(texto, title="Menu", border_style="green"))
        print('\033[33m1\033[m - \033[36mConsultar livros disponíveis\033[m')

    def pedir_senha(self):
        password = input('Digite sua senha: ')
        self.senha.append(password)
    # Essa funcionalidade será executada sempre no inicio do programa
    # A primeira vez pedirá uma "Nova Senha"

'''
    def alterar_senha():


    def consultar_saldo():

    def saque():
    # Aqui será executado o saque, dependendo da quantidade de dinheiro no caixa

    def deposito():
    # Aqui o depósito é ilimitado, dependendo do dinheiro do usuário'''



console = Console()
console.print(Panel("Seja Bem-Vindo ao Banco Python", style="green"))

caixa_eletronico = CaixaEletronico()
caixa_eletronico.pedir_senha()

for i in track(range(10), description="Processando..."):
    time.sleep(0.25)

while True:
    caixa_eletronico.mostrar_menu()
    escolha = int(input('Sua opção: '))
