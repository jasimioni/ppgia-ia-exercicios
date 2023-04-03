
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# Estudante 'é-um' AbstractEspecialista
class Estudante(AbstractEspecialista):

    @property
    def eh_ativado(self):
        if 'potencia' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('potencia')
        return ['potencia', p , '=', (p[0] ** p[1])]

    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)

