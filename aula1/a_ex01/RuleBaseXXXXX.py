import sys
sys.path.append('..')

from ExpertSystem.api.esBooleanRuleBase import BooleanRuleBase
from ExpertSystem.api.esRuleVariable import RuleVariable
from ExpertSystem.api.esCondition import Condition
from ExpertSystem.api.esRule import Rule
from ExpertSystem.api.esClause import Clause

class RuleBaseXXXXX:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):
        var0 = RuleVariable(self.br, "var0")
        var0.set_labels("00 11")
        var0.set_prompt_text("Qual é o valor de var0 [00,11]?")

        var1 = RuleVariable(self.br, "var1")
        var1.set_labels("11 22")
        var1.set_prompt_text("Qual é o valor de var1 [11,22]?")

        var3 = RuleVariable(self.br, "var3")
        var3.set_labels("XXX ZZZ")
        var3.set_prompt_text("Qual é o valor de var3 [XXX,ZZZ]?")

        c_equals = Condition("=")
        c_more_then = Condition(">")
        c_less_than = Condition("<")

        Regra00 = Rule(self.br, "Regra 00",
                       [Clause(var0, c_equals, "00")],
                       Clause(var1, c_equals, "aa"))

        Regra01 = Rule(self.br, "Regra 01",
                       [Clause(var1, c_equals, "aa")],
                       Clause(var3, c_equals, "ZZZ"))

        return self.br

    def demo_fc(self, LOG):
        LOG.append(
            " --- Ajustando valores para XXXXXXX para demo ForwardChain ---")
        self.br.set_variable_value("var0", "00")
        self.br.set_variable_value("var1", "aa")
        self.br.set_variable_value("var3", None)
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append(
            " --- Ajustando valores para XXXXX para demo BackwardChain ---")
        self.br.set_variable_value("var0", None)
        self.br.set_variable_value("var1", None)
        self.br.set_variable_value("var3", None)
        self.br.display_variables(LOG)
