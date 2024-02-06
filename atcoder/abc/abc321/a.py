n = list(map(int,input()))

for x,nx in zip(n,n[1:]):
    if x <= nx:
        print("No")
        exit()
print("Yes")