n = int(input())
for i in range(max(n,100),1000):
    if (i%10) == (i//100) * ((i//10)%10):
        print(i)
        exit()
