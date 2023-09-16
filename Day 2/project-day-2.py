
# tip calculator

print("Welcome to the tip calculator")

bill=float(input("What was the total bill?\n"))

percentage=int(input("What percentage tip would you like to give?10,12 or 15?\n"))

person=int(input("How many people to split the bill?\n"))


pay=((bill*percentage/100)+bill)/person

print(f"Each person should pay: ${round(pay,2)}")