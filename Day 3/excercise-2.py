# BMi calculator 2.0

weight=float(input("Enter your weight in kg: \n"))

height=float(input("Enter your height in m: \n"))

bmi=weight/(height**2)

if bmi<18.5:
    print(f"Tour BMI is {bmi}, and you are 'Underweight'")
elif bmi>18.5 and bmi<25:
    print(f"Tour BMI is {bmi}, and you are 'Normal Weight'")
elif bmi>25 and bmi<30:
    print(f"Tour BMI is {bmi}, and you are 'Overweight'")
elif bmi>30 and bmi<35:
    print(f"Tour BMI is {bmi}, and you are 'Obese'")
else:
    print(f"Tour BMI is {bmi}, and you are 'Clinically Obese'")