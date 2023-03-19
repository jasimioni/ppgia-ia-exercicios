import sys
sys.path.append('..')

from ExpertSystem.api.esMenu import APP
from RuleBaseCinema import RuleBaseCinema

class Main:
    def __init__(self):
        self.app = APP("Rule Application")

    def main(self):
        try:
            # RuleBaseCinema recebe dois parâmetros:
            # o primeiro é nome da base de regras e
            # o segundo é lista de várias presentes na base de regras.
            # Essas variáveis fazem parte dos possíveis objetivos
            brCinema = RuleBaseCinema("Como ir ao Cinema",
                                      "[deslocamento, meioDeTransporte] :")
            self.app.add_rule_base(brCinema)
            self.app.menu()
        except Exception as e:
            print("Exception: RuleApp ", e.with_traceback())


if __name__ == '__main__':
    Main().main()
