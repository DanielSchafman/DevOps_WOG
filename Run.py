import GuessGame
import Welcome
import GameLoader
import MemoryGame
import CurrencyGame
class Run():
    def run(self):
        welcome_message = Welcome.Welcome()
        player_name = welcome_message.message()
        game_loader = GameLoader.GameLoader()
        game_type = game_loader._get_game()
        game_difficulty = game_loader._get_difficulty()

        if(game_type == 1):
            play_memory_game = MemoryGame.MemoryGame()
            play_memory_game._present_numbers(game_difficulty)
            play_memory_game._get_choice()
            play_memory_game._is_choice_correct(player_name,game_difficulty)
        elif(game_type == 2):
            play_guess_game = GuessGame.Play()
            play_guess_game.user_choice(player_name,game_difficulty)
        elif(game_type == 3):
            play_currency_game = CurrencyGame.PlayCurrencyRoulette()
            play_currency_game._get_money_interval()
            play_currency_game._check_if_guess_correct(player_name,game_difficulty)


