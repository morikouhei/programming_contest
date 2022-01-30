X = input()
X = [int(x) for x in X]

ans = []
s = sum(X)
now = sum(X)
for x in X[::-1]:
    ans.append(now%10)
    s -= x
    now = now//10+s
    
if now:
    ans.append(now)
print(*ans[::-1],sep="")

