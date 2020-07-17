n = int(input())

count = [0]*(n+1)

for x in range(1,105):
    for y in range(1,105):
        for z in range(1,105):
            ans = (x+y)**2+(y+z)**2+(z+x)**2
            if ans%2 == 0 and ans//2 <= n:
                count[ans//2] += 1
for i in count[1:]:
    print(i)