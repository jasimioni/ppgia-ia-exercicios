#!/usr/bin/env python3

import sys
sys.path.append('..')

from planning.paip.gps import gps

### Inclua abaixo a definição para o problema
### descrito no arquivo "Exercicio_gerador_de_plano_de_ensino.docx"

problem = {
    "init": [
                "c-000:não é ainda capaz de construir uma solução de problemas usando redes de objetos",
                "c-001:está matriculado em uma disciplina de programação",
                "c-002:está matriculado em uma disciplina de rede semântica",
                "c-003:está matriculado em uma disciplina de grafos",
                # "c-1:constrói algoritmos"
            ],
    "finish": [ "c-12:construói solução de problemas usando redes de objetos" ],
    "ops": [
        {
            "action": "a-00 : cursar lógica matemática básica",
            "preconds": ["c-001:está matriculado em uma disciplina de programação"],
            "add": ["c-0:opera conceitos básicos da lógica matemática"], 
            "delete": [""]
        },
        { 
            "action": "a-01 : cursar lógica de programação",
            "preconds": ["c-0:opera conceitos básicos da lógica matemática"],
            "add": ["c-1:constrói algoritmos"],
            "delete": [""]
        },
        { 
            "action": "a-02 : cursar programar computadores",
            "preconds": ["c-1:constrói algoritmos"],
            "add": ["c-2:constrói programas"],
            "delete": [""]
        },
        { 
            "action": "a-03 : aprender representar problemas em grafos",
            "preconds": ["c-003:está matriculado em uma disciplina de grafos"],
            "add": ["c-3:representa problemas em grafos"],
            "delete": [""]
        },
        { 
            "action": "a-04 : aprender implementar mecanismos de busca em grafos",
            "preconds": [
                "c-2:constrói programas", 
                "c-3:representa problemas em grafos"
            ],
            "add": ["c-4:implementa mecanismos de busca em grafos"],
            "delete": [""]
        },
        { 
            "action": "a-05 : aprender redes semânticas e hierarquias: é-um e faz-parte-de",
            "preconds": ["c-002:está matriculado em uma disciplina de rede semântica"],
            "add": ["c-5:constrói hierarquias: é-um e faz-parte-de"],
            "delete": [""]
        },
        { 
            "action": "a-06 : aprender programar hierarquias  de classes e composições",
            "preconds": [
                "c-5:constrói hierarquias: é-um e faz-parte-de",
                "c-4:implementa mecanismos de busca em grafos"
            ],
            "add": ["c-6:implementa hierarquias  de classes e composições"],
            "delete": [""]
        },
        { 
            "action": "a-07 : aprender implementar redes de objetos",
            "preconds": ["c-6:implementa hierarquias  de classes e composições"],
            "add": ["c-7:implementa redes de objetos"],
            "delete": [""]
        },
        { 
            "action": "a-08 : aprender implementar estratégias de raciocínio",
            "preconds": ["c-7:implementa redes de objetos"],
            "add": ["c-8:implementa estratégias de raciocínio"],
            "delete": [""]
        },
        { 
            "action": "a-09 : aprender criar componentes de software",
            "preconds": ["c-8:implementa estratégias de raciocínio"],
            "add": ["c-9:cria componentes de software"],
            "delete": [""]
        },
        { 
            "action": "a-10 : aprender implementar testes unitários",
            "preconds": ["c-9:cria componentes de software"],
            "add": ["c-10:implementa testes unitários"],
            "delete": [""]
        },
        { 
            "action": "a-11 : aprender implementar testes de integração",
            "preconds": ["c-10:implementa testes unitários"],
            "add": ["c-11:implementa testes de integração"],
            "delete": [""]
        },
        { 
            "action": "a-12 : candidatar-se para desenvolvedor de solução de IA",
            "preconds": ["c-11:implementa testes de integração"],
            "add": ["c-12:construói solução de problemas usando redes de objetos"],
            "delete": ["c-000:não é ainda capaz de construir uma solução de problemas usando redes de objetos"]
        }
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
