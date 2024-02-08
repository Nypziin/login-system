from Sistema import Sistema
from getpass4 import getpass


def start():
    print('------------------------------------------\n'
          'Bem-vindo ao sistema de login\n'
          'Selecione uma das opções abaixo:\n'
          '[1] - Login\n'
          '[2] - Cadastrar')

    while True:
        opcao = input("Digite sua opção: ")
        if opcao == '1' or opcao == '2':
            if opcao == '1':
                usuario = input('Digite seu nome de usuário: ')
                senha = getpass('Digite sua senha: ')
                return opcao, usuario, senha
            else:
                usuario = input('Digite o nome do novo usuário: ')
                senha = getpass('Digite uma senha forte: ')
                return opcao, usuario, senha
        print('Opção inválida!')


class Main:
    def main(self):
        informacoes = start()
        sistema = Sistema(informacoes[1], informacoes[2])

        if informacoes[0] == '1':
            if sistema.login()[1]:
                print('------------------------------------------')
                print(sistema.login()[0])
            else:
                print('------------------------------------------')
                print(sistema.login()[0])
                self.main()
        else:
            print(sistema.cadastrar())


Main().main()



