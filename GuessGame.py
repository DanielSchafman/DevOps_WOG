from Input import ConsoleInput
from Output import PrintOutput
from GetSecret import Getsecret
from Score import Score
class Play:
    def __init__(self):
        self._get_input = ConsoleInput()
        self._print_prompt = PrintOutput()
        self.secret_generator = Getsecret()
        self._add_player_score = Score()

    def user_choice(self,name, difficulty):
        user_input = self._get_input._get_user_input("Please pick a number between 1 and {}\n".format(difficulty))
        user_input = self._get_input._validate_int(user_input,1,difficulty)
        
        self.secret = self.secret_generator._generate_secret(difficulty)
        self._is_choice_correct(user_input,self.secret,name,difficulty)


    def _is_choice_correct(self,user_input,secret,name,difficulty):
        if(int(user_input) == (secret)):
            self._print_prompt._print_prompt("Win!!!!!")
            self._add_player_score.adding_player_score(name,difficulty)
            return True
        else:
            self._print_prompt._print_prompt("Wrong! the right guess is {}".format(self.secret))
            return False