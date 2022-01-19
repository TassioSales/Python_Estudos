from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome,idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} ja está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def mostra(self):
        print(f"Nome:{self.nome}")

    def comer(self, alimento="Comida"):
        if self.comendo:
            print(f"{self.nome} ja esta comendo")
            return

        if self.falando:
            print(f"{self.nome} nao pode comer falando")
            return

        print(f"{self.nome} esta comendo {alimento}")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo.")
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
