#   A program to complete the value of an investment
#   carried 10 years into the future
#   by Saketh Gudla, Jun 13, 2023

def main():
    print("This program calculates the future value of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the amount of years: "))

    for i in range(year):
        principal = principal * (1 + apr)

    print("The value in", year, "years is: " , principal)

main()
