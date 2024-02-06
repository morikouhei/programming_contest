n = int(input())
S = input()

ans = 0

lines = S.split("<")

for l in lines:
    ans += (len(l) * (len(l)+1))//2
print(ans)