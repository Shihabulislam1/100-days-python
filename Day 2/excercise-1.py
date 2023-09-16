# Finding sum of first n digits of a number

num = input("Enter your  number: ")
digit = int(input("Enter the digits of the number you want to add: "))

sum = 0

num_s = str(num)

if digit <= len(num_s):
    for i in range(digit):
        sum = sum+int(num_s[i])

    print("Sum of the first "+str(digit)+" of the number is: "+str(sum))

else:
    print("You have entered a digit greater than the length of the number")
