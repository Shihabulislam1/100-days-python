
row1=["🅾️","🅾️","🅾️"]
row2=["🅾️","🅾️","🅾️"]
row3=["🅾️","🅾️","🅾️"]

map=[row1,row2,row3]
print(map)
print(f"{row1}\n{row2}\n{row3}")

pos=str(input("Where do you want to put the treasure? "))

col=int(pos[0])-1
row=int(pos[1])-1

map[row][col]="❌"

print(f"{row1}\n{row2}\n{row3}")