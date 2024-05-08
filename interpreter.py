from nodes import *
from values import Number, Variable

class Interpreter:
    def __init__(self):
        pass

    # Takes in node and adds the type of node to a string to determine which type
    # of node attributes we will use
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
        
    def visit_NumNode(self, node):
        return Number(node.value)

    def visit_VarNode(self, node):
        return Variable(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MulNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")
        
    def visit_ModNode(self, node):
        try:
            return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")
        
    def visit_PosNode(self, node):
        return self.visit(node.node)

    def visit_NegNode(self, node):
        return Number(-self.visit(node.node).value)

    # def visit_EquNode(self, node):
    #     self.visit(node.node_a).value = self.visit(node.node_b).value
    #     return Number(self.visit(node.node_a).value)
