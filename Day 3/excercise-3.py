# determin leap year

year = int(input("Enter the Year: \n"))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not leap year")

    else:
        print(*f"{year} is a leap year")

else:
    print(f"{year} is not leap year")
