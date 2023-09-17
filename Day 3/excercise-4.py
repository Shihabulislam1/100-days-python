
print("Welcome to Python Pizza Deliveries!\n")

size=str(input("What size pizza do you wanr? S, M, or L\n"))

add_pepparoni=input("Do you want pepparoni? Y or N\n")

extra_cheese=input("Do you want extra cheese? Y or N\n")

bill=0

if size=="S":
    bill=15
    if add_pepparoni=="Y":
        bill+=2
    if extra_cheese=="Y":
        bill+=1
    print(f"Your final bill is: ${bill}")

elif size=="M":
    bill=20
    if add_pepparoni=="Y":
        bill+=3
    if extra_cheese=="Y":
        bill+=1
    print(f"Your final bill is: ${bill}")

elif size=="L":
    bill=25
    if add_pepparoni=="Y":
        bill+=3
    if extra_cheese=="Y":
        bill+=1
    print(f"Your final bill is: ${bill}")