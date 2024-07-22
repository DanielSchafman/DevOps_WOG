from Input import ConsoleInput
from Output import PrintOutput


class Welcome:
    def __init__(self):
        self._get_input = ConsoleInput()
        self._print_prompt = PrintOutput()
       

    def message(self):
        self.name = self._get_input._get_user_input("Please enter your name:\n")
        self._print_prompt._print_prompt("Hello {} and welcome to the world of games(WoG)\nHere you can find many cool games to play.\n".format(self.name))
        return self.name