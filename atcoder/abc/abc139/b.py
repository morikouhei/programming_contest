a,b = map(int,input().split())
count = 0
now = 1
while now < b:
    count += 1
    now += (a-1)
print(count)