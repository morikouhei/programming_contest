p = int(input())

fact = [1]
for i in range(1,11):
    fact.append(fact[-1]*i)
ans = 0
for i in fact[::-1]:
    ans += p//i
    p %= i
print(ans)