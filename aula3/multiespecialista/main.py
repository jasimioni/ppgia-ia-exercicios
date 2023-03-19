#!/usr/bin/env python3

import sys
sys.path.append('..')

from multiespecialista.blackboard.QuadroNegro import QuadroNegro
from multiespecialista.controlador.Controlador import Controlador
from multiespecialista.geradordetarefa.GeradorDeTarefa import GeradorDeTarefa
from multiespecialista.especialista.Aluno import Aluno
from multiespecialista.especialista.Estudante import Estudante
from multiespecialista.especialista.Professor import Professor
from multiespecialista.especialista.SuperAluno import SuperAluno
from multiespecialista.especialista.SuperEstudante import SuperEstudante

if __name__ == '__main__':

    quadro_negro = QuadroNegro()
    GeradorDeTarefa = GeradorDeTarefa(quadro_negro)

    quadro_negro.adicionaEspecialista( Aluno(quadro_negro) )
    quadro_negro.adicionaEspecialista( Estudante(quadro_negro) )
    quadro_negro.adicionaEspecialista( Professor(quadro_negro) )

    quadro_negro.adicionaEspecialista( SuperAluno(quadro_negro) )
    quadro_negro.adicionaEspecialista( SuperEstudante(quadro_negro) )

    contribuicoes = Controlador(quadro_negro, GeradorDeTarefa, 120).loop()

    for x in contribuicoes:
        print(x)
