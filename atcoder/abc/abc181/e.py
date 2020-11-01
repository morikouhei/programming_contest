n,m = map(int,input().split())
h = [-10**20]+list(map(int,input().split()))
w = list(map(int,input().split()))
h.append(10**20)
h.sort()
w.sort()

ans = 10**20
even = [0]
for i in range(1,n,2):
    even.append(h[i+1]-h[i])
odd = [0]
for i in range(n,1,-2):
    odd.append(h[i]-h[i-1])

for i in range(1,len(even)):
    even[i] += even[i-1]
    odd[i] += odd[i-1]

now = 0
for i in w:
    while h[now] < i:
        now += 1
    if now%2:
        count = even[now//2]+h[now]-i+odd[(n-now)//2]
    else:
        count = even[now//2-1]+i-h[now-1]+odd[(n-now+1)//2]
    ans = min(ans,count)
    
print(ans)