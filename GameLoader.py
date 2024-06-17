from Input import ConsoleInput
from Output import PrintOutput


class GameLoader:
    def __init__(self):
        self.game_input = ConsoleInput()
        self.game_output = PrintOutput()


    def load_game(self):
        user_input = self.game_input._get_user_input("""Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have tp guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")
        
        if user_input is None or self.game_input._validate_int(user_input,1,3) == False:
            self.game_output._print_prompt("Invalid game choice")
            return None
        
        difficulty = self.game_input._get_user_input("Please choose game difficulty from 1 to 5:\n")

        if difficulty is None or self.game_input._validate_int(difficulty,1,5) == False:
            self.game_output._print_prompt("Invalid difficulty choice")
            return None

        self.game_output._print_prompt("Game choice: {0}, Difficulty: {1}".format(user_input,difficulty))
        return user_input,difficulty
 
