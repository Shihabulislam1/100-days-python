
lover1=str(input("Enter your Name:\n"))

lover2=str(input("Enter your Crush's Name:\n"))

lover1=lover1.lower()
lover2=lover2.lower()

t=lover1.count("t")+lover2.count("t")+lover1.count("r")+lover2.count("r")+lover1.count("u")+lover2.count("u")+lover1.count("e")+lover2.count("e")

l=lover1.count("l")+lover2.count("l")+lover1.count("o")+lover2.count("o")+lover1.count("v")+lover2.count("v")+lover1.count("e")+lover2.count("e")

total=int(str(t)+str(l))
print(total)
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")

elif total>40 and total<50:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"Your score is {total}.")