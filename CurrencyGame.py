from Input import ConsoleInput
from Output import PrintOutput
from GetSecret import Getsecret
from Score import Score
import creds
import requests

class PlayCurrencyRoulette:
    def __init__(self):
        self._user_input = ConsoleInput()
        self._print_output = PrintOutput()
        self._random_generator = Getsecret()
        self._add_player_score = Score()
        self.api_key = creds.APIKEY
        self.base_currency = "USD"
        self.target_currency = "ILS"
        self.max_random = 100

    def get_exchange_rate(self, api_key, base_currency, target_currency):
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency={base_currency}&currencies={target_currency}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and 'data' in data:
            return data['data'][target_currency]
        else:
            raise Exception("Error fetching exchange rate: " + data.get("error", "Unknown error"))

    def convert_currency(self, amount, exchange_rate):
        return amount * exchange_rate

    def _get_money_interval(self):
        self.random_num = self._random_generator._generate_secret(self.max_random)
        self.user_input = self._user_input._get_user_input(f"The number is {self.random_num}$ how much do you think it's in shekels?")
        self.user_input = self._user_input._validate_float(self.user_input, 1, 400)
        return self.user_input, self.random_num

    def _check_if_guess_correct(self,name ,difficulty):
        exchange_rate = self.get_exchange_rate(self.api_key, self.base_currency, self.target_currency)
        amount_in_ils = self.convert_currency(self.random_num, exchange_rate)
        margin = 5 - difficulty
        if amount_in_ils <= (self.user_input - margin) or amount_in_ils >= (self.user_input + margin):
            print(f"Nope! The correct amount is {amount_in_ils:.2f} ILS.")
            return False
        else:
            print(f"You win! The correct amount is {amount_in_ils:.2f} ILS.")
            self._add_player_score.adding_player_score(name,difficulty)
            return True
        