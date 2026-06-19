
        # for item in operands: 
        #     result = result + item

from utils.mathUtils import add,subtract,multiply,division

# import utils.mathUtils as math !not recommended


#from utils.mathUtils import * #!should also not be used



def calculator(operands,operator="+"):
    result  = 0
    if operator == "+":
        result = add(operands) #result += item
    elif operator == "-":
        result = subtract(operands) #result -= item
        #return result
    elif operator == "*":
        result = multiply(operands)
    elif operator == "/":
        result = division(operands) #result += item
    else:
        print("Operator entry is not valid!")
    
    print("End of function!")
    return result
