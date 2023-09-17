# Odd or Even

number = float(input("Enter the number to be evaluated as odd or even : \n"))

number = round(number, 0)

if number % 2 == 0:
    print(str(number)+" is Even")
elif number % 2 != 0:
    print(str(number)+" is Odd")
