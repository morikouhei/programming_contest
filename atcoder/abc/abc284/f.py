def Z_algorithm(s):
    
    n = len(s)
    if n == 0:
        return []

    z = [0]*n
    j = 0
    for i in range(1,n):
        z[i] = 0 if j + z[j] <= i else min(j+z[j]-i,z[i-j])
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
            if j + z[j] < i + z[i]:
                j = i
    z[0] = n
    return z



n = int(input())
T = input()

fr = T+T[::-1]
ba = T[::-1]+T
front = Z_algorithm(fr)
back = Z_algorithm(ba)


a1 = [0]*(2*n)
a2 = [0]*(2*n)
for i,a in enumerate(front[2*n:]):

    if a == 0:
        continue
    a1[-1-i] = a

for i,a in enumerate(back[2*n:]):
    if a == 0:
        continue
    a2[i] = a


for i in range(n,2*n):
    a = a1[i]

    if a < i-n+1:
        continue
    b = a2[n-(2*n-i-1)]
    if b < n - (i-n+1):
        continue
    print(T[i-n+1:i+1][::-1])
    print(i-n+1)
    exit()
print(-1)
