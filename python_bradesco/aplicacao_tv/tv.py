class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20
        self.volume_min = 0
        self.volume_max = 100

    def aumenta_volume(self, valor=1):
        """Aumenta o volume em 'valor' unidades, sem ultrapassar o volume máximo."""
        novo_volume = self.volume + valor
        self.volume = min(novo_volume, self.volume_max)
        return self.volume

    def diminui_volume(self, valor=1):
        """Diminui o volume em 'valor' unidades, sem ficar abaixo do volume mínimo."""
        novo_volume = self.volume - valor
        self.volume = max(novo_volume, self.volume_min)
        return self.volume

    def troca_canal(self, canal):
        """Troca para o canal especificado, se estiver na lista de canais."""
        if canal in self.lista_de_canais:
            self.canal_atual = canal
            return True
        return False

    def sintoniza_canal(self, canal):
        """Adiciona um novo canal à lista de canais, se ainda não existir."""
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)
            self.lista_de_canais.sort()
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

    def aumenta_volume(self, valor=1):
        """Aumenta o volume usando o controle remoto."""
        return self.tv.aumenta_volume(valor)

    def diminui_volume(self, valor=1):
        """Diminui o volume usando o controle remoto."""
        return self.tv.diminui_volume(valor)

    def troca_canal(self, canal):
        """Troca de canal usando o controle remoto."""
        return self.tv.troca_canal(canal)

    def sintoniza_canal(self, canal):
        """Sintoniza um novo canal usando o controle remoto."""
        return self.tv.sintoniza_canal(canal)

    def lista_canais(self):
        """Retorna a lista de canais disponíveis."""
        return self.tv.lista_de_canais

    def __str__(self):
        return f"Controle Remoto para {self.tv.fabricante} {self.tv.modelo}"
