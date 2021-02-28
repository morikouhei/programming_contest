from collections import defaultdict
dic = defaultdict(int)
n = int(input())

ans = n
for i in range(2,n):
    if dic[i] == 1:
        continue
    if i**2 > n:
        break

    for j in range(2,n):
        if i**j > n:
            break
        if i**j <= n:
            dic[i**j] = 1
            ans -= 1
    
print(ans)