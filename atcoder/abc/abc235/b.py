n = int(input())
H = list(map(int,input().split()))

ans = 0
for i in range(1,n):
    if H[ans] < H[i]:
        ans += 1
    else:
        break
print(H[ans])