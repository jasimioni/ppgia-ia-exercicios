#!/usr/bin/env python3

import sys
sys.path.append('..')

from planning.paip.gps import gps

'''
Esse plano descreve os passos para implantar uma solução Kubernetes. A solução
depende de um Hardware para ser instalada, o qual precisa ser adquirido, instalado
e testado. Após isso é necessário instalar e configurar a aplicação, implementar
as políticas de segurança e finalmente gerar a documentação para uso.
'''

problem = {
    "init": ["C-00: Não possui ambiente Kubernetes",
             "C-01: Feita a requisição de compras do Hardware",
             "C-02: Feita a requisição de compras do Software",
             "C-03: Feita a requisição de compras dos serviços"],
    "finish": ["C-16: Possui ambiente Kubernetes instalado e operacional"],
    "ops": [
        {
            "action": "A-01: Preparar ambiente físico para instalação do Hardware",
            "preconds" : [],
            "add": ["C-04: Ambiente físico preparado"],
            "delete": [""]
        },
        {
            "action": "A-02: Receber o Hardware",
            "preconds": ["C-01: Feita a requisição de compras do Hardware"],
            "add": ["C-05: Hardware recebido"],
            "delete": []
        },
        {
            "action": "A-03: Fazer a instalação física do Hardware",
            "preconds": [
                "C-04: Ambiente físico preparado",
                "C-05: Hardware recebido"
            ],
            "add": ["C-06: Hardware instalado"],
            "delete": []

        },
        {
            "action": "A-04: Fazer o setup do Hardware",
            "preconds": ["C-06: Hardware instalado"],
            "add": ["C-07: Setup de Hardware feito"],
            "delete": []
        },
        {
            "action": "A-05: Realizar testes de Hardware",
            "preconds": ["C-07: Setup de Hardware feito"],
            "add": ["C-08: Testes de Hardware realizados"],
            "delete": []
        },
        {
            "action": "A-06: Receber o Software",
            "preconds": ["C-02: Feita a requisição de compras do Software"],
            "add": ["C-09: Software recebido"],
            "delete": []
        },
        {
            "action": "A-07: Fazer a instalação do Software",
            "preconds": [
                "C-09: Software recebido",
                "C-03: Feita a requisição de compras dos serviços",
                "C-08: Testes de Hardware realizados"
            ],
            "add": ["C-10: Software instalado"],
            "delete": []
        },
        {
            "action": "A-08: Aplicar as configurações de segurança recomendadas",
            "preconds": ["C-10: Software instalado"],
            "add": ["C-11: Configurações de segurança aplicadas"],
            "delete": []
        },
        {
            "action": "A-09: Realizar testes de Software",
            "preconds": ["C-11: Configurações de segurança aplicadas"],
            "add": ["C-12: Testes de Software realizados"],
            "delete": []
        },
        {
            "action": "A-10: Criar credenciais dos administradores",
            "preconds": ["C-12: Testes de Software realizados"],
            "add": ["C-13: Credenciais de administradores criadas"],
            "delete": []
        },
        {
            "action": "A-11: Criar credenciais dos usuários",
            "preconds": ["C-12: Testes de Software realizados"],
            "add": ["C-14: Credenciais de usuários criadas"],
            "delete": []
        },
        {
            "action": "A-12: Gerar a documentação do sistema",
            "preconds": [
                "C-13: Credenciais de administradores criadas",
                "C-14: Credenciais de usuários criadas"
            ],
            "add": ["C-15: Documentação gerada"],
            "delete": []
        },
        {
            "action": "A-13: Entregar sistema configurado",
            "preconds": ["C-15: Documentação gerada"],
            "add": ["C-16: Possui ambiente Kubernetes instalado e operacional"],
            "delete": ["C-00: Não possui ambiente Kubernetes"]
        },
    ]
}

def main():
    start = problem['init']
    finish = problem['finish']
    ops = problem['ops']
    msg="Você deve: "

    plan = gps(start, finish, ops, msg)
    if plan is not None:
        for action in plan:
            print (action)
    else:
        print('O plano não foi gerado')

if __name__ == '__main__':
    main()
