n = int(input())
s = set()
S = input()
s.add((0,0))
x,y = 0,0

for i in S:
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    else:
        y -= 1
    
    if (x,y) in s:
        print("Yes")
        exit()
    s.add((x,y))
print("No")