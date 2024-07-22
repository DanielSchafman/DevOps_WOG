import random

class Getsecret():
    def __init__(self):
        self.secret = None

    def _generate_secret(self,max):
        self.secret = random.randint(1,int(max))
        return self.secret
