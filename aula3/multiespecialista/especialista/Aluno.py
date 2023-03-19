
import random
from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista

# Aluno 'é-um' AbstractEspecialista
class Aluno(AbstractEspecialista):

    # Testa se a especialidade do 'Aluno' está presente na lista de problemas a serem resolvidos
    @property
    def eh_ativado(self):
        if 'soma' in self.QuadroNegro.estadoCompartilhado['problemas']:
            return True
        else:
            return False

    # implementação da expertise do 'Aluno'; como ele realiza sua tarefa
    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa('soma')
        return ['soma', p , '=', (p[0]+p[1])]

    # Quanto a realização da tarefa so Aluno contribui com o avanço geral da solução do problema.
    @property
    def progresso(self):
        return random.randint(1, 5)

    # Atualiza o quadro-negro com a contribuição do 'Aluno'
    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)
