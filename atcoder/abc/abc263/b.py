n = int(input())
P = list(map(int,input().split()))

now = n-2
count = 1
while True:
    if P[now] == 1:
        break
    now = P[now]-2
    count += 1
print(count)