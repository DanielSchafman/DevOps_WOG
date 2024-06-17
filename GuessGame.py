from abc import ABC,abstractmethod
import random

class Input(ABC):
    @abstractmethod
    def _get_user_input(self,prompt):
        pass


class ConsoleInput(Input):
    def _get_user_input(self,prompt):
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            return None


class Get_secret():
    def __init__(self):
        self.secret = None

    def _generate_secret(self,difficulty):
        self.secret = random.randint(1,difficulty)
        return self.secret


class Play:
    def __init__(self, input_method: Input, secret_generator: Get_secret):
        self.input_method = input_method
        self.secret_generator = secret_generator

    def choice(self, difficulty) -> None:
        self.secret_generator._generate_secret(difficulty)
        user_choice = self.input_method._get_user_input("Please pick a number between 1 and {}\n".format(difficulty))
        if user_choice is None:
            print("Invalid choice")
            return

        self._is_choice_correct(user_choice)


    def _is_choice_correct(self,user_input):
        if(user_input == self.secret_generator.secret):
            print("Win!!!!!")
        else:
            print("Wrong! the secret is {}".format(self.secret_generator.secret))