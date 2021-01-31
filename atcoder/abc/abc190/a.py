a,b,c = map(int,input().split())
for i in range(200):
    for j in range(2):
        if c:
            if b:
                b -= 1
            else:
                print("Takahashi")
                exit()
        else:
            if a:
                a -= 1
            else:
                print("Aoki")
                exit()
        c = (c+1)%2


