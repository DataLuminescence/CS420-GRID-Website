from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
	NUM     = 0
	ADD     = 1
	SUB     = 2
	MUL     = 3
	DIV     = 4
	MOD     = 5
	LPA     = 6
	RPA     = 7
	VAR     = 8

# Create token class which has a type, a value and returns 
@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")