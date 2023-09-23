

scores=input("Enter score: \n").split(" ")

for s in range(0,len(scores)):
    scores[s]=int(scores[s])

print(f"Student's scores: {scores}")

max=0

for m in scores:
    if m>max:
        max=m

print(f"Max score: {max}")