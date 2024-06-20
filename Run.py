import GuessGame
import Welcome
import GameLoader
import MemoryGame

class Run():
    def run(self):
        welcome_message = Welcome.Welcome()
        welcome_message.message()
        game_loader = GameLoader.GameLoader()
        game_type = game_loader._get_game()
        game_difficulty = game_loader._get_difficulty()

        if(game_type == 1):
            play_memory_game = MemoryGame.MemoryGame()
            play_memory_game._present_numbers(game_difficulty)
        elif(game_type == 2):
            play_guess_game = GuessGame.Play()
            play_guess_game.user_choice(game_difficulty)
        elif(game_type == 3):
            pass

