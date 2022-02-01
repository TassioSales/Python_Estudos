from classes import Escritor,Caneta, MaquinaDeEscrever


escritor = Escritor('Joãozinho')
caneta =  Caneta("Bic")
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina

escritor.ferramenta.escrever()