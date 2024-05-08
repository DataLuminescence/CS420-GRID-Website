from tokens import TokenType
from nodes import *
STATE   = dict()

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.__next__()
		self.variables = {}  # Use a dictionary to store variables

	def raise_error(self):
		raise Exception("Invalid syntax")
    
    # Used to move to the next character in the text until
	# there is no next character
	def __next__(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	# If current token is not None return result of expr(). This allows
	# us to groups our expressions and iterate through the tokens to
	# find more expressions
	def parse(self):
		result = self.expr()
		if self.current_token is not None:
			self.raise_error()
		return result

	# Calls term function to follow order of operations. Once term() 
	# and factor() are done complete ADD and SUB operations that are
	# not in parenthesis
	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.ADD, TokenType.SUB):
			if self.current_token.type == TokenType.ADD:
				self.__next__()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.SUB:
				self.__next__()
				result = SubNode(result, self.term())

		return result

	# Calls factor function to follow order of operations. Once 
	# complete evaluate MUL DIV and MOD operations that are not
	# in parenthesis
	def term(self):
		result = self.factor()

		while self.current_token != None and self.current_token.type in (TokenType.MUL, TokenType.DIV, TokenType.MOD):
			if self.current_token.type == TokenType.MUL:
				self.__next__()
				result = MulNode(result, self.factor())
			elif self.current_token.type == TokenType.DIV:
				self.__next__()
				result = DivNode(result, self.factor())
			elif self.current_token.type == TokenType.MOD:
				self.__next__()
				result = ModNode(result, self.factor())
				
		return result

	# Makes sure operations inside parenthesis are evalatuated
	# first. As well as setting the value of variables and
	# unary operations, in order to follow order of operations 
	def factor(self):
		token = self.current_token
		if token is not None and token.type == TokenType.VAR:
			print("token is not None 1")
			var_name = token.value
			self.__next__()
			if var_name in self.variables:
				print("token is not None 2")
				return self.variables[var_name]
			else:
				print("token is not None 3")
				result = self.expr()
				self.variables[var_name] = result
				print("token is not None 4")
				return result

		elif token.type == TokenType.LPA:
			self.__next__()
			result = self.expr()

			if self.current_token.type != TokenType.RPA:
				self.raise_error()
			
			self.__next__()
			return result

		elif token.type == TokenType.NUM:
			self.__next__()
			return NumNode(token.value)

		elif token.type == TokenType.ADD:
			self.__next__()
			return PosNode(self.factor())
		
		elif token.type == TokenType.SUB:
			self.__next__()
			return NegNode(self.factor())
		
		self.raise_error()