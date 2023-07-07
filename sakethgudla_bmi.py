import math

def main():
    while True:
        print("Welcome to the BMI calculator!")
        
        h = eval(input("Please enter your height in centimeters? "))
        if (h <= 1):
            main()
                
        w = eval(input("Please eneter your weight in kilograms? "))
        
        bmi = ((w / (h*h)) * 10000)
        rbmi = round(bmi, 1)
        print("Your BMI is ", rbmi)
        
        if (rbmi < 18.5):
            print("You're really skinny")
            
        elif (rbmi >= 18.5) and (rbmi <= 24.9):
            print("Normal weight")
            
        elif (rbmi >= 25.0) and (rbmi <= 29.9):
            print("You're fat")
            
        elif (rbmi >= 30):
            print("You're overweight")
        
main()