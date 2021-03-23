n = int(input())

use = [0]*(n+1)
use[1] = 1
for i in range(1,n+1):
    for j in range(i*2,n+1,i):
        use[j] = use[i]+1
print(*use[1:])