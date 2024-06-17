import GuessGame
import Welcome
import GameLoader

if __name__ == "__main__":
    welcome_message = Welcome.Welcome()
    welcome_message.message()
    game_loader = GameLoader.GameLoader()
    game_details = game_loader.load_game()
    #if game_details:
     #   print(f"Game choice: {game_details[0]}, Difficulty: {game_details[1]}")
      #  input_method = GuessGame.ConsoleInput()
       # secret_generator = GuessGame.Get_secret()
        #game = GuessGame.Play(input_method,secret_generator)
        #game.choice(game_details[1])