
import random
from multiespecialista.especialista.Estudante import Estudante

### SuperEstudante 'é-um' Estudante
class SuperEstudante(Estudante):

    ### especialize o SuperEstudante para ele retorne o menor valor de uma lista
    ### ....

    ### função que implementar a contribuição do 'super estudante'.
    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
