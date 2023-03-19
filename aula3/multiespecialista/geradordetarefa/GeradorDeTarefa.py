
import random

class GeradorDeTarefa(object):

    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    def soma(self):
        p = [random.randint(1, 40), random.randint(1, 40)]
        return [p[0],p[1]]  # Ex: p = [14, 34]

    def potencia(self):
        p = [random.randint(1, 40), random.randint(1, 4)]
        return [p[0],p[1]]  # Ex: p = [20, 3]

    def raiz(self):
        p = [random.randint(1, 40), random.randint(1, 4)]
        return [p[0], p[1]]  # Ex: p = [34, 2]


    def maximo(self):
        p = []
        for i in range(random.randint(3, 10)):
            p.append(random.randint(1, 100))
        return p         # p = [95, 34, 54, 3]

    def minimo(self):
        p = []
        for i in range(random.randint(3, 10)):
            p.append(random.randint(1, 100))
        return p         # p = [95, 34, 54, 3]

    def adicionaTarefa(self):
        self.QuadroNegro.adicionaTarefa('soma', self.soma())
        self.QuadroNegro.adicionaTarefa('potencia',self.potencia())
        self.QuadroNegro.adicionaTarefa('raiz',self.raiz())
        self.QuadroNegro.adicionaTarefa('maximo',self.maximo())
        self.QuadroNegro.adicionaTarefa('minimo',self.minimo())
