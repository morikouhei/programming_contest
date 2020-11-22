s,p = map(int,input().split())
for i in range(1,int(p**0.5)+5):
    if p%i == 0:
        if p//i + i == s:
            print("Yes")
            exit()
print("No")