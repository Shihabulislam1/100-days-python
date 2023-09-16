# Find BMI

weight=float(input("Enter Your Weifht in Kg: "))

height=float(input("Enter your Height in meters: "))


bmi=weight/(height**2)
# first 2 digit after decimal
bmi=round(bmi,2)

print("Your BMI is: "+str(bmi))