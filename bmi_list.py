import math

output = ["You are ", "Please eneter your height in centimeters: ", "Please enter your weight in kilograms: "]

print("Welcome to the BMI calculator!")

def main():
    while True:
        
        h = eval(input(output[1]))  
        w = eval(input(output[2]))
        
        if ((h <= 1) or (w <= 1)):
            main()
        
        bmi = ((w / (h*h)) * 10000)
        rbmi = round(bmi, 1)
        print("Your BMI is",rbmi)
        
        if (rbmi < 18.5):
            print(output[0] + "really skinny")
            
        elif (rbmi >= 18.5) and (rbmi <= 24.9):
            print(output[0] + "healthy")
            
        elif (rbmi >= 25.0) and (rbmi <= 29.9):
            print(output[0] + "fat")
            
        elif (rbmi >= 30):
            print(output[0] + "overweight")
            
        
        
main()