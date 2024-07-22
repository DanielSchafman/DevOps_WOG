from Input import ConsoleInput
from Output import PrintOutput
from GetSecret import Getsecret
from Score import Score
import time


class MemoryGame:
    def __init__(self):
        self._user_input = ConsoleInput()
        self._print_prompt = PrintOutput()
        self._secret_generator = Getsecret()
        self._add_player_score = Score()
        self._list_of_numbers = []
        self._list_user_input = []
        self._top_number = 101

    def _present_numbers(self,difficulty):
        for i in range(int(difficulty)):
            self.secret = self._secret_generator._generate_secret(self._top_number)
            self._list_of_numbers.append(self.secret)
        
        print(self._list_of_numbers,end="",flush=True)
        time.sleep(2)
        self._print_prompt._print_prompt("\r                                ")
        return None

    def _get_choice(self):
        user_input = self._user_input._get_user_input("Enter what you saw:\n")
        self._list_user_input = user_input.split(" ")

        if(len(self._list_user_input) != len(self._list_of_numbers)):
            self._print_prompt._print_prompt("Wrong number of inputs :@")
            return self._get_choice()
        
        self._list_after_validation = self._user_input._validate_list_of_int(self._list_user_input,1,self._top_number)
        return None
    
    def _is_choice_correct(self,name,difficulty):
        for num in range(len(self._list_after_validation)):
            if(int(self._list_after_validation[num]) != int(self._list_of_numbers[num])):
                self._print_prompt._print_prompt("Wrong :@\n the list is {}".format(self._list_of_numbers))
                break
            elif(num == len(self._list_after_validation) -1 and int(self._list_after_validation[num]) == int(self._list_of_numbers[num])):
                self._print_prompt._print_prompt("You win!!")
                self._add_player_score.adding_player_score(name,difficulty)
