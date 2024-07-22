from abc import ABC, abstractmethod

class ConsoleInput():
    def _get_user_input(self,prompt):
        user_input = input(prompt)
        return user_input
    
    def _validate_int(self,user_input,min,max):
        while True:
            try:
                user_input = user_input.strip()
                if not user_input.isdigit():
                    raise ValueError("{} Input is not a digit".format(user_input))
                user_input = int(user_input)
                if min <= user_input <= max:
                    break
                else:
                    user_input = self._get_user_input("{} Invalid input: number out of range :@\n try again:\n".format(user_input))
            except:
                user_input = self._get_user_input("{} Invalid input: not a valid number :@\n try again:\n".format(user_input))
        return user_input
    
    def _validate_list_of_int(self, user_list, min, max):
        list_after_validation = []
        for item in user_list:
            validated_item = self._validate_int(item, min, max)
            list_after_validation.append(validated_item)
        return list_after_validation
    
    def is_float(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _validate_float(self,user_input, min_val, max_val):
        while True:
            try:
                user_input = user_input.strip()
                if not self.is_float(user_input):
                    raise ValueError("{} Input is not a valid float".format(user_input))
                user_input = float(user_input)
                if min_val <= user_input <= max_val:
                    break
                else:
                    user_input = self._get_user_input("{} Invalid input: number out of range :@\n try again:\n".format(user_input))
            except ValueError as e:
                user_input = self._get_user_input("{} Invalid input: not a valid number :@\n try again:\n".format(user_input))
        return user_input