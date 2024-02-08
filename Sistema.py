class Sistema:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def cadastrar(self):
        with open('usuarios.txt', 'a+') as arquivo:
            arquivo.write(f'{self.usuario},{self.senha}\n')
            msg = 'Cadastro efetuado com sucesso!'
            return msg

    def login(self):
        try:
            with open('usuarios.txt', 'r+') as arquivo:
                for usuario in arquivo:
                    if usuario.split(',')[0] == self.usuario:
                        if int(usuario.split(',')[1]) != int(self.senha):
                            msg = 'Senha Incorreta'
                            return msg, False
                        else:
                            msg = 'Login efetuado com sucesso!'
                            return msg, True

            msg = 'Usuário não encontrado!'
            return msg, False

        except FileNotFoundError:
            msg = 'Usuário não encontrado!'
            return msg, False







