from calculator import calculator
import json 

operands = []
calculations = []

while True: 
    quit_programm = input("Do you want to quit [quit]").lower()
    #print(quit_programm)
    if quit_programm == "quit":
        break
    while True:
        operand = input("Enter the Operand or [quit]\n")
        if operand.lower() == "quit":
            print("Continue with calculation")
            break
        if not isinstance(float(operand),float): 
            print("The input entered is not an operand.")
            break
        else:
            operands.append(float(operand))

  
    if len(operands) > 2:
        name_calculation = input("Enter a name for the calculation!\n>>")
        operator = input("Enter the operator\n")
        result = calculator(operands,operator)
        single_calculation = {}
        single_calculation["name"] = name_calculation
        single_calculation["operator"] = operator
        single_calculation["operands"] = operands
        single_calculation["result"] = result
        
        calculations.append(single_calculation)
        operands = []
    else:
        print("Please restart. Too few operands!")
      
      
#https://www.geeksforgeeks.org/python/json-dump-in-python/  
with open("./live-code/function-module/data.json", "w") as data_file:
    json.dump(calculations, data_file)
    
    data_file.close()
    
print(calculations)

