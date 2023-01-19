n = int(input())
P = list(map(int,input().split()))

ans = []
def swap(x,y):
    P[x],P[y] = P[y],P[x]

def calc(m,ind):
    if m == 1:
        ans.append(["A",ind+1])
        swap(ind,ind+1)
    if m == 2:
        ans.append(["B",ind+1])
        swap(ind,ind+2)


for i,p in enumerate(P):
    if i%2 != p%2:
        continue
    for j in range(i-2,-1,-2):
        calc(2,j)


for i in range(0,n-1,2):
    if P[i]%2 == i%2:
        calc(1,i)

for i in range(1,n+1)[::-1]:
    for j in range(n):
        if P[j] == i:
            ind = j
    
    while ind+2 < n and P[ind] > P[ind+2]:
        calc(2,ind)
        ind += 2
        
print(len(ans))
for i in ans:
    print(*i)