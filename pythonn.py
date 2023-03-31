def takeInput():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+,-,*,/): ")
    return (num1, num2, operator)

def displayResult():
    num1, num2, operator = takeInput()
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator")
        return
    
    print(f"{num1} {operator} {num2} = {result}")

displayResult()
