from theHundredTree.app import node

def buildTemplate(start, end):
    root = node.Node(None)
    aux = root
    
    for num in range(start, end):
        aux.left = node.Node(str(num))
        
        if (num + 1 == end):
            aux.right = node.Node(str(end))
        else:
            aux.right = node.Node(None)
        
        aux = aux.right
    
    return root
    

def validate(min, max, sum):
    errors = []
    if (min < 0 or min > 5):
        errors.append('Put a minimum value between 1 and 5')
    if (max < 5 or max > 9):
        errors.append('Put a maximum value between 5 and 9')
    if (sum < 50 or sum > 150):
        errors.append('Put a sum value between 50 and 150')
    return errors
