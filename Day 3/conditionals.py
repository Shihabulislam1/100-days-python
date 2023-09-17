
# If else

height = float(input("Enter your Height in centimeter: \n"))
age = int(input("Enter your Age: \n"))
if height >= 120:
    print("You can ride the rollercoster")
    if age > 18:
        print("For above age 18 ticket price is $12")
    elif age < 12:
        print("For below age 12 ticket price is $5")
    elif age > 12 and age < 18:
        print("For age 12-18 ticket price is $7")

else:
    print("Sorry, you have to grow taller before you can ride.")
