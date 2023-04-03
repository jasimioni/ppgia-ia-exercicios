
import random
from multiespecialista.especialista.Aluno import Aluno

# SuperAluno 'é-um' Aluno
class SuperAluno(Aluno):

    ### especialize o SuperAluno para ele retorne o maior valor de uma lista
    ### ....

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
