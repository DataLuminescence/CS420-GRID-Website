from dataclasses import dataclass

# Used to return a string representation of number node
@dataclass
class NumNode:
	value: any

	def __repr__(self):
		return f"{self.value}"

# Used to return a string representation of variable node
@dataclass
class VarNode:
	value: any

	def __repr__(self):
		return f"{self.value}"

# Used to return a string representation when adding
@dataclass
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

# Used to return a string representation when subtracting
@dataclass
class SubNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

# Used to return a string representation when multiplying
@dataclass
class MulNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

# Used to return a string representation when dividing
@dataclass
class DivNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"
	
# Used to return a string representation when moding
@dataclass
class ModNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}%{self.node_b})"

# Used to return a string representation when performing
# positive unary operations
@dataclass
class PosNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"

# Used to return a string representation when performing
# negative unary operations	
@dataclass
class NegNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"
	
# # Used to set the value of a variable
# @dataclass
# class EquNode:
# 	# Variable
# 	node_a: any
# 	# Term, Variable, or expression
# 	node_b: any

# 	def __repr__(self):
# 		return f"({self.node_a}={self.node_b})"
