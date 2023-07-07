import math

def trae():
    while True:
        print("1.(+) 2.(-) 3.(*) 4.(/) 5.(^) 6.Square Root")
        n = eval(input("Select an operation:"))
    
        match n:
            case 1:
                num1 = eval(input("Enter first number:"))
                num2 = eval(input("Enter second number:"))
                print(num1 + num2)
        
            case 2:
                num1 = eval(input("Enter first number:"))
                num2 = eval(input("Enter second number:"))
                print(num1 - num2)
    
            case 3:
                num1 = eval(input("Enter first number:"))
                num2 = eval(input("Enter second number:"))
                print(num1 * num2)
    
            case 4:
                num1 = eval(input("Enter first number:"))
                num2 = eval(input("Enter second number:"))
                print(num1 / num2)
    
            case 5:
                num1 = eval(input("Enter first number:"))
                num2 = eval(input("Enter second number:"))
                print(math.pow(num1, num2))
    
            case 6:
                num = eval(input("Enter number:"))
                print(math.sqrt(num))
        
        next_calc = (input("Next Calculation? (yes/no):" ))
        if (next_calc == "yes"):
            trae()
        else:
            quit()
        
    
trae()