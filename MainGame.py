import Live
import GuessGame

if __name__ == "__main__":
    welcome_message = Live.Welcome()
    welcome_message._get_user_input()
    welcome_message.message()


    game_loader = Live.GameLoader()
    game_details = game_loader.load_game()
    if game_details:
        print(f"Game choice: {game_details[0]}, Difficulty: {game_details[1]}")
        input_method = GuessGame.ConsoleInput()
        secret_generator = GuessGame.Get_secret()
        game = GuessGame.Play(input_method,secret_generator)
        game.choice(game_details[1])