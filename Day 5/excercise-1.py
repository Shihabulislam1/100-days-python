
students_heights=input("Enter the heights of students: ").split(" ")

for i in range(0,len(students_heights)):
    students_heights[i]=int(students_heights[i])

print(students_heights)

total_height=0
total_s=0

for h in students_heights:
    total_height+=h
    total_s+=1

print(total_height)
print(total_s)

print(f"Average={round(total_height/total_s)}")