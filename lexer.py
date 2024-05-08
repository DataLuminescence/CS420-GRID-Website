from tokens import Token, TokenType

NONCHAR = ' \n\t'
DIGITS  = '0123456789'
STATE   = dict()

class Lexer:
	
    # Takes in text and iterated through it advance will
	# allow us to move to the next character in text
    def __init__(self, expression):
        self.expression = iter(expression)
        self.__next__()
        self.variables = {}  # Use a dictionary to store variables

    # Used to move to the next character in the text until
	# there is no next character
    def __next__(self):
        try:
            self.current_char = next(self.expression)
        except StopIteration:
            self.current_char = None

    # Gets token based on if the character is an operator,
	# number or variable. 
    def get_token(self):
        while self.current_char is not None:

            if self.current_char in NONCHAR:
                self.__next__()

            if self.current_char.isalpha():
                return self.set_variable()
            
			# If decimal number or char in DIGITS call get_number function
			# to make sure its the first decimal or to keep track of first
			# digit of number in a string 
            if self.current_char == '.' or self.current_char.isdigit():
                yield self.get_number()
            elif self.current_char.isalpha():
                yield self.set_variable()
            elif self.current_char == '+':
                self.__next__()
                yield Token(TokenType.ADD)
            elif self.current_char == '-':
                self.__next__()
                yield Token(TokenType.SUB)
            elif self.current_char == '*':
                self.__next__()
                yield Token(TokenType.MUL)
            elif self.current_char == '/':
                self.__next__()
                yield Token(TokenType.DIV)
            elif self.current_char == '%':
                self.__next__()
                yield Token(TokenType.MOD)
            elif self.current_char == '(':
                self.__next__()
                yield Token(TokenType.LPA)
            elif self.current_char == ')':
                self.__next__()
                yield Token(TokenType.RPA)
            else:
                raise Exception(f"Error: Invalid operator '{self.current_char}'")

    # Iterates through program name to make sure only valid 
    # characters are present. 
    def get_grid_name(self):

        while self.current_char != "{" and self.current_char in NONCHAR:
            self.__next__()

    # Once a number or decimal character has been identified, this
	# function makes sure there is only one decimal point per number
	# and iterates through the rest of the text until either the end 
	# of the number is reached or when a second erroneous decimal 
	# presents itself
    def get_number(self):
		
        decimal_counter = 0
        num_str = self.current_char
        self.__next__()

        # As long as the current char is not None, and is a decimal, digit, keep looping
        while self.current_char != None and (self.current_char == '.' or self.current_char.isdigit()):
            
            if self.current_char == '.':
                decimal_counter += 1
                if decimal_counter > 1:
                    break
            
            num_str += self.current_char
            self.__next__()

        # Adds leading zero or trailing zero for numbers starting or
        # ending with decimal
        if num_str.startswith('.'):
            num_str = '0' + num_str
        if num_str.endswith('.'):
            num_str += '0'

        # Uses token class to return the token type and string 
        # representation of operand
        return Token(TokenType.NUM, float(num_str))
    
    def set_variable(self):
        var_name = self.current_char
        self.__next__()

        while (self.current_char != None and self.current_char != "=" and 
               (self.current_char.isalpha() or self.current_char.isdigit())):
            var_name += self.current_char
            self.__next__()

        if(self.current_char == "="):
            self.__next__()
            var_value = ""
            while(self.current_char is not None):
                var_value += self.current_char
                self.__next__()
                print(var_value)

            self.variables[var_name] = var_value
            return Token(TokenType.VAR, var_name)
        else:
            return Token(TokenType.VAR, var_name)

    def get_variable(self):

        # If ther current char is a letter, find if variable exists in state and if so find value
        if self.current_char in STATE:
            print(STATE[self.current_char])
            var_val = STATE[self.current_char]
            return Token(TokenType.VAR, str(var_val))
        else:
            print("Error: Var not found")