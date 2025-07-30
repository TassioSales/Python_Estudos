import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4/3) * math.pi*(self.raio**3)
        return vol

    def area(self):
        area = 4 * math.pi*(self.raio**2)
        return area

if __name__ == "__main__":
    bola1 = Esfera("vermelha", 4)
    bola2 = Esfera("azul", 7)

    print(f"O volume da bola1 é: {bola1.volume()}")
    print(f"A area superficial da bola1 é:{bola1.area()}cm^2")
    print(f"O volume da bola2 é: {bola2.volume()}")
    print(f"A area superficial da bola2 é:{bola2.area()}cm^2")

    print(bola1.volume())
    print(Esfera.volume(bola1))