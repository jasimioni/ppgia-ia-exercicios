from multiespecialista.especialista.AbstractEspecialista import AbstractEspecialista
import random
import re


# TextSplitter:
# Esse especialista converte uma string em uma lista de palavras. Adiciona uma tarefa
# Na fila para converter para lower_case
class TextSplitter(AbstractEspecialista):
    def __init__(self, quadro_negro):
        super().__init__(quadro_negro)
        self.tarefa = 'split_text'
        self.prox_tarefa = 'lower_case'

    @property
    def eh_ativado(self):
        if len(self.QuadroNegro.estadoCompartilhado['instancias-de-problemas'][self.tarefa]): 
            return True 
        return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa(self.tarefa)

        splitted = p.split()

        self.QuadroNegro.adicionaTarefa(self.prox_tarefa, splitted)
        return [self.tarefa, p , '=', splitted]

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)

# CaseLower:
# Esse especialista converte todas as palavras da lista para lower_case
# Adiciona uma tarefa para remover acentuação e pontuação
class CaseLower(AbstractEspecialista):
    def __init__(self, quadro_negro):
        super().__init__(quadro_negro)
        self.tarefa = 'lower_case'
        self.prox_tarefa = 'remove_accent'

    @property
    def eh_ativado(self):
        if len(self.QuadroNegro.estadoCompartilhado['instancias-de-problemas'][self.tarefa]): 
            return True 
        return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa(self.tarefa)
        lc = [ item.lower() for item in p ]
        self.QuadroNegro.adicionaTarefa(self.prox_tarefa, lc)
        return [self.tarefa, p , '=', lc]

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)

# AccentPonctuationRemover:
# Esse especialista remove os acentos e a pontuação
# Adiciona a tarefa de contar as palavras
class AccentPonctuationRemover(AbstractEspecialista):
    def __init__(self, quadro_negro):
        super().__init__(quadro_negro)
        self.tarefa = 'remove_accent'
        self.prox_tarefa = 'count_words'

    @property
    def eh_ativado(self):
        if len(self.QuadroNegro.estadoCompartilhado['instancias-de-problemas'][self.tarefa]): 
            return True 
        return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa(self.tarefa)
        na = [ re.sub(r'[áàâäã]', 'a', item) for item in p ]
        na = [ re.sub(r'[éèêëẽ]', 'e', item) for item in na ]
        na = [ re.sub(r'[íìîïĩ]', 'i', item) for item in na ]
        na = [ re.sub(r'[óòôöõ]', 'o', item) for item in na ]
        na = [ re.sub(r'[úùûüũ]', 'u', item) for item in na ]
        na = [ re.sub(r'[,.:]', '', item) for item in na ]
        self.QuadroNegro.adicionaTarefa(self.prox_tarefa, na)
        return [self.tarefa, p , '=', na]

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)

# WordCounter:
# Esse especialista conta as palavras e constroi um dicionário com eleas
# Adiciona uma tarefa para ordenar a contagem
class WordCounter(AbstractEspecialista):
    def __init__(self, quadro_negro):
        super().__init__(quadro_negro)
        self.tarefa = 'count_words'
        self.prox_tarefa = 'order_list'

    @property
    def eh_ativado(self):
        if len(self.QuadroNegro.estadoCompartilhado['instancias-de-problemas'][self.tarefa]): 
            return True 
        return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa(self.tarefa)

        word_count = {}
        for word in p:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

        self.QuadroNegro.adicionaTarefa(self.prox_tarefa, word_count)
        return [self.tarefa, p , '=', word_count]

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)

# WordSorter:
# Esse especialista ordena os dicionários de acordo com a contagem 
# de cada palavra, e converte em uma lista
class WordSorter(AbstractEspecialista):
    def __init__(self, quadro_negro):
        super().__init__(quadro_negro)
        self.tarefa = 'order_list'

    @property
    def eh_ativado(self):
        if len(self.QuadroNegro.estadoCompartilhado['instancias-de-problemas'][self.tarefa]): 
            return True 
        return False

    @property
    def expertise(self):
        p = self.QuadroNegro.pegaTarefa(self.tarefa)
        sorted_words = [ [ key, p[key] ] for key in sorted(p, key=lambda x: (-p[x], x)) ]

        return [self.tarefa, p , '=', sorted_words]

    @property
    def progresso(self):
        return random.randint(1, 5)

    def contribui(self):
        self.QuadroNegro.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.QuadroNegro.atualizaProgresso(self.progresso)