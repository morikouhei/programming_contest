t = int(input())
for _ in range(t):
    n,k,z = map(int,input().split())
    ans = 0
    l = list(map(int,input().split()))
    cum = [0]
    ma = [0]
    for i in range(k+1):
        cum.append(cum[-1]+l[i])
        if i == 0:
            ma.append(0)
        else:
            ma.append(max(ma[-1],l[i]+l[i-1]))
    ans = cum[-1]
    for i in range(1,z*2+1):
        if k-i < 1:
            break
        #print(cum[k-i+1],ma[k-i+1])
        if i%2:
            count = cum[k-i+1]+l[k-1-i]
            
            count += (i//2)*ma[k+1-i]
        else:
            count = cum[k-i+1] + (i//2)*ma[k+1-i]
        #print(i,count)
        ans = max(ans,count)
    print(ans)

