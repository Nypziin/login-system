import json


class Sistema:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def cadastrar(self):

        dados_cadastro = {
            'usuario': self.usuario,
            'senha': self.senha
        }

        try:
            with open('usuarios.json', 'r'):
                pass

        except (FileNotFoundError, FileExistsError):
            with open('usuarios.json', 'w'):
                pass

        finally:
            with open('usuarios.json', 'r+') as arquivo:
                try:
                    dados = json.load(arquivo)
                except json.decoder.JSONDecodeError:
                    dados = []

                dados.append(dados_cadastro)

                arquivo.seek(0)
                json.dump(dados, arquivo, indent=4)
                arquivo.truncate()

                msg = 'Cadastro efetuado com sucesso!'
                return msg

    def login(self):
        try:
            with open('usuarios.json', 'r+') as arquivo:
                dados = json.load(arquivo)

                for usuario in dados:
                    if usuario['usuario'] == self.usuario:
                        if int(usuario['senha']) != int(self.senha):
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







