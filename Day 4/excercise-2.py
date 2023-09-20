
import random as rd


names=input("Give me everyday's names, separated by comas: ").split(", ")

num=rd.randint(0,len(names)-1)

print(f"{names[num]} will pay the bill today!")

# choice() function
person=rd.choice(names)
print(f"{person} will pay the bill today!")