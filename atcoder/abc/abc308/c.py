from functools import cmp_to_key
n = int(input())
AB = []
for i in range(n):
    a,b = map(int,input().split())
    AB.append([a,b,i+1])

def cmp(a,b):
    return -1 if a[0]*(b[0]+b[1]) > b[0]*(a[0]+a[1]) else 1


AB = sorted(AB,key=cmp_to_key(cmp))

for a,b,i in AB:
    print(i)

