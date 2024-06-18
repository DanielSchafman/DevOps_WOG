import random

class Getsecret():
    def __init__(self):
        self.secret = None

    def _generate_secret(self,difficulty):
        self.secret = random.randint(1,int(difficulty))
        return self.secret
