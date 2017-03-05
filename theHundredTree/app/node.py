
class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.expressions = []
    
    def __str__(self):
        if (self.value is None): return ''
        else: return self.value
    
    def getExpression(self):
        return self.__convert(self, '')
    
    def __convert(self, theNode, expression):
        if (theNode is None): return expression
        else: return theNode.__convert(theNode.left, expression) + str(theNode) + theNode.__convert(theNode.right, expression)
    
    def getPossibilities(self, sum, operators):
        self.__getPossibilities(self, self, sum, operators)
        
    def __getPossibilities(self, current, root, sum, operators):
        for op in operators:
            if (current.right is not None):
                current.value = op
                self.__getPossibilities(current.right, root, sum, operators)
            else:
                theTree = root.getExpression()
                if (eval(theTree) == sum): root.expressions.append(theTree)
                break
