
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# Professor 'é-um' AbstractEspecialista
class Professor(AbstractEspecialista):

    @property
    def eh_ativado(self):
        return True if 'raiz' in self.QuadroNegro.estadoCompartilhado['problemas'] else False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('raiz')
        return ['raiz', p ,'=', (p[0] ** (1.0 / p[1]))]

    @property
    def progresso(self):
        return random.randint(12, 120)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
