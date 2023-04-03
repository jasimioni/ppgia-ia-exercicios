# Tarefa é carregar um texto do arquivo e adicionar com a primeira ação
# Que é split_text

import random

def get_random_quote():
    with open('quotes.txt') as quotes:
        lines = quotes.readlines()
        line_num = random.randint(0, len(lines) - 1)
        return lines[line_num].rstrip()

class GeradorDeTarefa(object):
    def __init__(self, quadro_negro):
        self.QuadroNegro = quadro_negro

    def adicionaTarefa(self):
        self.QuadroNegro.adicionaTarefa('split_text', get_random_quote())
