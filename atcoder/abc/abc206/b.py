n = int(input())
ans = 0
for i in range(1,n+5):
    ans += i
    if ans >= n:
        print(i)
        exit()