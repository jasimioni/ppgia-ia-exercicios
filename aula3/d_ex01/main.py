#!/usr/bin/env python3

import sys

from multiespecialista.blackboard.QuadroNegro import QuadroNegro
from multiespecialista.controlador.Controlador import Controlador
from multiespecialista.geradordetarefa.GeradorDeTarefa import GeradorDeTarefa
from multiespecialista.especialista.Especialistas import *

if __name__ == '__main__':

    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista( TextSplitter(quadro_negro) )
    quadro_negro.adicionaEspecialista( CaseLower(quadro_negro) )
    quadro_negro.adicionaEspecialista( WordCounter(quadro_negro) )
    quadro_negro.adicionaEspecialista( AccentPonctuationRemover(quadro_negro) )
    quadro_negro.adicionaEspecialista( WordSorter(quadro_negro) )

    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 120).loop()

    for x in contribuicoes:
        print("--------------------------------------------")
        print(x)