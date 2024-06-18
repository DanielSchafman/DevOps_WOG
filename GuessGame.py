from Input import ConsoleInput
from Output import PrintOutput
from GetSecret import Getsecret
class Play:
    def __init__(self):
        self._get_input = ConsoleInput()
        self._print_prompt = PrintOutput()
        self.secret_generator = Getsecret()


    def user_choice(self, difficulty):
        user_input = self._get_input._get_user_input("Please pick a number between 1 and {}\n".format(difficulty))
        if(self._get_input._validate_int(user_input,1,difficulty) == False):
            return self.user_choice(difficulty)

        self.secret = self.secret_generator._generate_secret(difficulty)
        self._is_choice_correct(user_input,self.secret)


    def _is_choice_correct(self,user_input,secret):
        if(int(user_input) == (secret)):
            self._print_prompt._print_prompt("Win!!!!!")
            return True
        else:
            self._print_prompt._print_prompt("Wrong! the right guess is {}".format(self.secret))
            return False