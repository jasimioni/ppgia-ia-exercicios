
# Alterações feitas:
# Adicionar tarefa / pegar tarefa trata as tarefas como listas ao invés de uma tarefa por tipo

class QuadroNegro(object):

    def __init__(self):
        self.especialistas = []
        self.estadoCompartilhado = {'problemas' : ['lower_case', 'split_text', 'count_words', 'remove_accent', 'order_list'],
                                    'instancias-de-problemas' : {
                                                                 'lower_case' : [],
                                                                 'split_text' : [],
                                                                 'count_words' : [],
                                                                 'remove_accent' : [],
                                                                 'order_list' : []
                                                                },
                                    'contribuicoes' : [],
                                    'progresso' : 0}

    def adicionaEspecialista(self, especialista):
        self.especialistas.append(especialista)

    def adicionaContribuicao(self, contribuicao):
        self.estadoCompartilhado['contribuicoes'] += contribuicao

    def atualizaProgresso(self, progresso):
        self.estadoCompartilhado['progresso'] += progresso

    def adicionaTarefa(self, tarefa, paramentros):
        self.estadoCompartilhado['instancias-de-problemas'][tarefa].append(paramentros)

    def pegaTarefa(self, tarefa):
        if len(self.estadoCompartilhado['instancias-de-problemas'][tarefa]):
            return self.estadoCompartilhado['instancias-de-problemas'][tarefa].pop(0)
        return None

    def mostraTarefas(self):
        print('instancias-de-problemas',self.estadoCompartilhado['instancias-de-problemas'])
