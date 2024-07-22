from Input import ConsoleInput
from Output import PrintOutput


class GameLoader:
    def __init__(self):
        self.game_input = ConsoleInput()
        self.game_output = PrintOutput()



    def _get_game(self):
        user_input = self.game_input._get_user_input("""Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have tp guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")
        
        user_input = self.game_input._validate_int(user_input,1,3)
        self.game_output._print_prompt("Game choice: {0}".format(user_input))
        return user_input
    
    def _get_difficulty(self):
        difficulty = self.game_input._get_user_input("Please choose game difficulty from 1 to 5:\n")
        difficulty = self.game_input._validate_int(difficulty,1,5)

        self.game_output._print_prompt("Difficulty: {0}".format(difficulty))
        return difficulty
 
