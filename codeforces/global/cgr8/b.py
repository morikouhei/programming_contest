n = int(input())
s = list("codeforces")
if n == 1:
    print(*s,sep="")
    exit()
for i in range(1,10000):
    if i**10 >= n:
        k = i
        break
k -= 1

for i in range(1,11):
    if (k+1)**(i)*(k**(10-i)) >= n:
        m = i
        break
ans = ""
for i in range(10):
    if i < m:
        ans += s[i]*(k+1)
    else:
        ans += s[i]*k
print(ans)