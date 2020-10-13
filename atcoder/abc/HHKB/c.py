n = int(input())
p = list(map(int,input().split()))

count = [0]*(2*10**5+5)
now = 0
for i in p:
    count[i] += 1
    while count[now] != 0:
        now += 1
    print(now)