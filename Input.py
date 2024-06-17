from abc import ABC, abstractmethod

class ConsoleInput():
    def _get_user_input(self,prompt):
        user_input = input(prompt)
        return user_input
    
    def _validate_int(self,user_input,min,max):
        try:
            self.user_input = int(user_input)
            return min <= self.user_input <= max
        except ValueError:
            return False

