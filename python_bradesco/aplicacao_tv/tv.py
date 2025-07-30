class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20

    def aumentaVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100
        return self.volume

    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0
        return self.volume

    def trocaCanal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal
            return True
        return False

    def sintonizaCanal(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)
            return True
        return False

    def __str__(self):
        return (f"TV {self.fabricante} {self.modelo}\n"
                f"Canal atual: {self.canal_atual or 'Nenhum'}\n"
                f"Volume: {self.volume}\n"
                f"Canais disponíveis: {', '.join(self.lista_de_canais) or 'Nenhum'}")


class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self):
        self.tv.aumentaVolume(90)

    def diminuiVolume(self):
        self.tv.diminuiVolume(90)

    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)
        
    def getListaCanais(self):
        return self.tv.lista_de_canais
        
    def getCanalAtual(self):
        return self.tv.canal_atual
        
    def getVolume(self):
        return self.tv.volume
