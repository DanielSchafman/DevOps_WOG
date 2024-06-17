from abc import ABC, abstractmethod

class  Input(ABC):
    def _get_user_input(self):
        pass

class Welcome(Input):
    def _get_user_input(self):
        self.name = input("Please enter your name:\n")

    def message(self):
        print ("Hello {} and welcome to the world of games(WoG)\nHere you can find many cool games to play.".format(self.name))

class GameLoader(Input):
    def load_game(self):
        game_choice = self._get_user_input("""Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have tp guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""", 1,3)
        
        if game_choice is None:
            print("Invalid gmae choice")
            return None
        
        difficulty = self._get_user_input("Please choose game difficulty from 1 to 5:\n", 1, 5)

        if difficulty is None:
            print("Invalid difficulty choice")
            return None

        return game_choice,difficulty
    
    def _get_user_input(self, prompt, min, max):
        user_input = input(prompt)
        if self._is_valid_choice(user_input,min,max):
            return int(user_input)
        else:
            return None
        
    def _is_valid_choice(self, user_input, min, max):
        try:
            choice = int(user_input)
            return min <= choice <= max
        except ValueError:
            return False
        
