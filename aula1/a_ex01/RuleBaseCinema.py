import sys
sys.path.append('..')

from ExpertSystem.api.esBooleanRuleBase import BooleanRuleBase
from ExpertSystem.api.esRuleVariable import RuleVariable
from ExpertSystem.api.esCondition import Condition
from ExpertSystem.api.esRule import Rule
from ExpertSystem.api.esClause import Clause

class RuleBaseCinema:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):
        distancia = RuleVariable(self.br, "distancia")
        distancia.set_labels("1 50")
        distancia.set_prompt_text("Qual é a distância até o cinema [1,50]?")

        deslocamento = RuleVariable(self.br, "deslocamento")
        deslocamento.set_labels("carro a-pe")
        deslocamento.set_prompt_text(
            "Qual é a forma de deslocameto [carro, a-pe]?")

        tempo = RuleVariable(self.br, "tempo")
        tempo.set_labels("0 60")
        tempo.set_prompt_text("Qual é o tempo disponível [1,60]?")

        local_do_cinema = RuleVariable(self.br, "localDoCinema")
        local_do_cinema.set_labels("centro bairro")
        local_do_cinema.set_prompt_text("Onde é o cinema [centro, bairro]]?")

        meio_de_transporte = RuleVariable(self.br, "meioDeTransporte")
        meio_de_transporte.set_labels(
            "taxi carro-proprio a-pe-triste a-pe-feliz")
        meio_de_transporte.set_prompt_text(
            "Qual é o meio de transporte [taxi, carro-proprio, a-pe-triste, a-pe-feliz]]?")

        clima = RuleVariable(self.br, "clima")
        clima.set_labels("ruim bom")
        clima.set_prompt_text("Como está o clima [bom, ruim]?")

        c_equals = Condition("=")
        c_more_then = Condition(">")
        c_less_than = Condition("<")

        Regra01 = Rule(self.br, "Regra 01",
                       [Clause(distancia, c_more_then, "5")],
                       Clause(deslocamento, c_equals, "carro"))

        Regra02 = Rule(self.br, "Regra 02",
                       [Clause(distancia, c_more_then, "1"),
                        Clause(tempo, c_less_than, "15")],
                       Clause(deslocamento, c_equals, "carro"))

        Regra03 = Rule(self.br, "Regra 03",
                       [Clause(distancia, c_more_then, "1"),
                        Clause(tempo, c_more_then, "15")],
                       Clause(deslocamento, c_equals, "a-pe"))

        Regra04 = Rule(self.br, "Regra 04",
                       [Clause(deslocamento, c_equals, "carro"),
                        Clause(local_do_cinema, c_equals, "centro")],
                       Clause(meio_de_transporte, c_equals, "taxi"))

        Regra05 = Rule(self.br, "Regra 05",
                       [Clause(deslocamento, c_equals, "carro"),
                        Clause(local_do_cinema, c_equals, "bairro")],
                       Clause(meio_de_transporte, c_equals, "carro-proprio"))

        Regra06 = Rule(self.br, "Regra 06",
                       [Clause(deslocamento, c_equals, "a-pe"),
                        Clause(clima, c_equals, "ruim")],
                       Clause(meio_de_transporte, c_equals, "a-pe-triste"))

        Regra07 = Rule(self.br, "Regra 07",
                       [Clause(deslocamento, c_equals, "a-pe"),
                        Clause(local_do_cinema, c_equals, "bom")],
                       Clause(meio_de_transporte, c_equals, "a-pe-feliz"))
        return self.br

    def demo_fc(self, LOG):
        LOG.append(
            " --- Ajustando valores para Transporte/Cinema para demo ForwardChain ---")
        self.br.set_variable_value("distancia", "2")
        self.br.set_variable_value("deslocamento", None)
        self.br.set_variable_value("tempo", "10")
        self.br.set_variable_value("localDoCinema", "centro")
        self.br.set_variable_value("meioDeTransporte", None)
        self.br.set_variable_value("clima", "ruim")
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append(
            " --- Ajustando valores para Transporte/Cinema para demo BackwardChain ---")
        self.br.set_variable_value("distancia", None)
        self.br.set_variable_value("deslocamento", None)
        self.br.set_variable_value("tempo", None)
        self.br.set_variable_value("localDoCinema", "centro")
        self.br.set_variable_value("meioDeTransporte", None)
        self.br.set_variable_value("clima", "ruim")
        self.br.display_variables(LOG)
