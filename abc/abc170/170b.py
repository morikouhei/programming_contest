x,y = map(int,input().split())

for i in range(x+1):
    for j in range(x+1):
        if i+j != x:
            continue
        if 2*i+4*j == y:
            print("Yes")
            exit()
print("No")