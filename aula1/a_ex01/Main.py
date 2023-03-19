import sys
sys.path.append('..')

from ExpertSystem.api.esMenu import APP
from RuleBaseXXXXX import RuleBaseXXXXX

class Main:
    def __init__(self):
        self.app = APP("Rule Application")

    def main(self):
        try:
            # RuleBaseXXXX recebe dois parâmetros:
            # o primeiro é nome da base de regras e
            # o segundo é lista de várias presentes na base de regras.
            # Essas variáveis fazem parte dos possíveis objetivos
            brCinema = RuleBaseXXXXX("Como XXXXXX",
                                      "[var1 var3] :")
            self.app.add_rule_base(brCinema)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e.with_traceback())


if __name__ == '__main__':
    Main().main()
