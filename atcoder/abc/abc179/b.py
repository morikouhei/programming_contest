n = int(input())
count = 0
for i in range(n):
    a,b = map(int,input().split())
    if a == b:
        count += 1
    else:
        if count >= 3:
            print("Yes")
            exit()
        count = 0
if count >= 3:
    print("Yes")
else:
    print("No")