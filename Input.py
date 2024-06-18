from abc import ABC, abstractmethod

class ConsoleInput():
    def _get_user_input(self,prompt):
        user_input = input(prompt)
        return user_input
    
    def _validate_int(self,user_input,min,max):
        if user_input.strip().isdigit() or user_input:
            user_input = int(user_input)
            if min <= user_input <= max:
                return True
            else:
                print("Invalid input: number out of range :@")
                return False
        else:
            print("Invalid input: not a valid number :@")
            return False