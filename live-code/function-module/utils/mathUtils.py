def add(operands: list) -> float|int:
    """Add multiple numbers together.

    @operands: a list of float numbers 
    
    @return: the sum
    """
    result = 0
    if len(operands) < 2:
        result = result + operands[0]
    else:
        for item in operands: 
            result = result + item     
    return result

def subtract(operands: list) -> float|int:
    result = operands[0]
    if len(operands) < 2:
        return result
    else:
        for item in operands: 
            result = result - item     
    return result

def multiply(operands: list) -> float|int:
    result = operands[0]
    if len(operands) < 2:
        return result
    for item in operands: 
        result = result * item 
    return result

def division(operands: list) -> float|int:
    result = operands[0]
    if len(operands) < 2:
        return result
    for item in operands: 
            result = result / item
    return result

def thisIsNotUsed():
    pass