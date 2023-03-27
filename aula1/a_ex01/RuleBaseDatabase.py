import sys
sys.path.append('..')

from ExpertSystem.api.esBooleanRuleBase import BooleanRuleBase
from ExpertSystem.api.esRuleVariable import RuleVariable
from ExpertSystem.api.esCondition import Condition
from ExpertSystem.api.esRule import Rule
from ExpertSystem.api.esClause import Clause

class RuleBaseDatabase:
    def __init__(self, nome, goals_list):
        self.br = BooleanRuleBase(nome)
        self.goals_list = goals_list

    def get_goal_list(self):
        return self.goals_list

    def create(self):
        armazenamento = RuleVariable(self.br, "armazenamento")
        armazenamento.set_labels(
            "lib client_server"
        )
        armazenamento.set_prompt_text(
            "Qual o modelo de armazenamento [lib, client_server]"
        )

        provedor = RuleVariable(self.br, "provedor")
        provedor.set_labels(
            "aws azure on_premises"
        )
        provedor.set_prompt_text(
            "Qual o provedor de nuvem [aws azure on_premises]"
        )

        tipo_de_banco = RuleVariable(self.br, "tipo_de_banco")
        tipo_de_banco.set_labels(
            "relacional nosql"
        )
        tipo_de_banco.set_prompt_text(
            "Qual o tipo de banco de dados [relacional nosql]"
        )

        licenciamento = RuleVariable(self.br, "licenciamento")
        licenciamento.set_labels(
            "comercial opensource"
        )
        licenciamento.set_prompt_text(
            "Qual o tipo de licenciamento desejado [comercial opensource]"
        )

        banco_de_dados = RuleVariable(self.br, "banco_de_dados")
        banco_de_dados.set_labels(
            "SQLite RocksDB RDS DynamoDB AzureSQL CosmosDB PostgreSQL MongoDB Oracle MarkLogic"
        )
        banco_de_dados.set_prompt_text(
            "Qual o modelo de banco desejado [SQLite RocksDB RDS DynamoDB AzureSQL CosmosDB PostgreSQL MongoDB Oracle MarkLogic]"
        )

        c_equals = Condition("=")
        c_more_then = Condition(">")
        c_less_than = Condition("<")

        Regra00 = Rule(self.br, "Regra 00",
                       [Clause(armazenamento, c_equals, "lib"),
                        Clause(tipo_de_banco, c_equals, "relacional")],
                       Clause(banco_de_dados, c_equals, "SQLite"))

        Regra01 = Rule(self.br, "Regra 01",
                       [Clause(armazenamento, c_equals, "lib"),
                        Clause(tipo_de_banco, c_equals, "nosql")],
                       Clause(banco_de_dados, c_equals, "RocksDB"))

        Regra02 = Rule(self.br, "Regra 02",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "aws"),
                        Clause(tipo_de_banco, c_equals, "relacional")],
                       Clause(banco_de_dados, c_equals, "RDS"))

        Regra03 = Rule(self.br, "Regra 03",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "aws"),
                        Clause(tipo_de_banco, c_equals, "nosql")],
                       Clause(banco_de_dados, c_equals, "DynamoDB"))

        Regra04 = Rule(self.br, "Regra 04",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "azure"),
                        Clause(tipo_de_banco, c_equals, "relacional")],
                       Clause(banco_de_dados, c_equals, "AzureSQL"))

        Regra05 = Rule(self.br, "Regra 05",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "azure"),
                        Clause(tipo_de_banco, c_equals, "nosql")],
                       Clause(banco_de_dados, c_equals, "CosmosDB"))

        Regra06 = Rule(self.br, "Regra 06",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "on_premises"),
                        Clause(licenciamento, c_equals, "opensource"),
                        Clause(tipo_de_banco, c_equals, "relacional")],
                       Clause(banco_de_dados, c_equals, "PostgreSQL"))

        Regra07 = Rule(self.br, "Regra 07",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "on_premises"),
                        Clause(licenciamento, c_equals, "opensource"),
                        Clause(tipo_de_banco, c_equals, "nosql")],
                       Clause(banco_de_dados, c_equals, "MongoDB"))

        Regra08 = Rule(self.br, "Regra 08",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "on_premises"),
                        Clause(licenciamento, c_equals, "comercial"),
                        Clause(tipo_de_banco, c_equals, "relacional")],
                       Clause(banco_de_dados, c_equals, "Oracle"))

        Regra09 = Rule(self.br, "Regra 09",
                       [Clause(armazenamento, c_equals, "client_server"),
                        Clause(provedor, c_equals, "on_premises"),
                        Clause(licenciamento, c_equals, "comercial"),
                        Clause(tipo_de_banco, c_equals, "nosql")],
                       Clause(banco_de_dados, c_equals, "MarkLogic"))

        Regra10 = Rule(self.br, "Regra 10",
                       [Clause(provedor, c_equals, "aws")],
                       Clause(licenciamento, c_equals, "comercial"))

        Regra11 = Rule(self.br, "Regra 11",
                       [Clause(provedor, c_equals, "azure")],
                       Clause(licenciamento, c_equals, "comercial"))

        Regra12 = Rule(self.br, "Regra 12",
                       [Clause(provedor, c_equals, "on_premises"),
                        Clause(armazenamento, c_equals, "lib")],
                       Clause(licenciamento, c_equals, "opensource"))

        Regra13 = Rule(self.br, "Regra 13",
                       [Clause(provedor, c_equals, "on_premises"),
                        Clause(armazenamento, c_equals, "client_server"),
                        Clause(banco_de_dados, c_equals, "PostgreSQL")],
                       Clause(licenciamento, c_equals, "opensource"))

        Regra14 = Rule(self.br, "Regra 14",
                       [Clause(provedor, c_equals, "on_premises"),
                        Clause(armazenamento, c_equals, "client_server"),
                        Clause(banco_de_dados, c_equals, "MongoDB")],
                       Clause(licenciamento, c_equals, "opensource"))

        Regra15 = Rule(self.br, "Regra 15",
                       [Clause(provedor, c_equals, "on_premises"),
                        Clause(armazenamento, c_equals, "client_server"),
                        Clause(banco_de_dados, c_equals, "Oracle")],
                       Clause(licenciamento, c_equals, "comercial"))

        Regra16 = Rule(self.br, "Regra 16",
                       [Clause(provedor, c_equals, "on_premises"),
                        Clause(armazenamento, c_equals, "client_server"),
                        Clause(banco_de_dados, c_equals, "MarkLogic")],
                       Clause(licenciamento, c_equals, "comercial"))
        
        return self.br

    def demo_fc(self, LOG):
        LOG.append(
            " --- Ajustando valores para Database para demo ForwardChain ---")
        self.br.set_variable_value("armazenamento", "client_server")
        self.br.set_variable_value("provedor", "aws")
        self.br.set_variable_value("licenciamento", None)
        self.br.set_variable_value("tipo_de_banco", "nosql")
        self.br.display_variables(LOG)

    def demo_bc(self, LOG):
        LOG.append(
            " --- Ajustando valores para Database para demo BackwardChain ---")
        self.br.set_variable_value("armazenamento", "client_server")
        self.br.set_variable_value("provedor", "aws")
        self.br.set_variable_value("licenciamento", None)
        self.br.set_variable_value("tipo_de_banco", "nosql")
        self.br.display_variables(LOG)
