import sys
sys.path.append('..')

from ExpertSystem.api.esMenu import APP
from RuleBaseDatabase import RuleBaseDatabase

class Main:
    def __init__(self):
        self.app = APP("Rule Application")

    def main(self):
        try:
            # RuleBaseXXXX recebe dois parâmetros:
            # o primeiro é nome da base de regras e
            # o segundo é lista de várias presentes na base de regras.
            # Essas variáveis fazem parte dos possíveis objetivos
            brDatabase = RuleBaseDatabase("Escolhendo seu banco de dados",
                                      "[licenciamento banco_de_dados] :")
            self.app.add_rule_base(brDatabase)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e.with_traceback())


if __name__ == '__main__':
    Main().main()
