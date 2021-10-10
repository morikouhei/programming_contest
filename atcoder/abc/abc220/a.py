a,b,c = map(int,input().split())
for i in range(a,b+1):
    if i%c:
        continue
    print(i)
    exit()
print(-1)