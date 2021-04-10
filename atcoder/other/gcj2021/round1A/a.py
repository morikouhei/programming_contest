
def solve():
    n = int(input())
    X = list(map(int,input().split()))
    count = 0
    now = 0
    for i in range(n):
        nex = X[i]
        #print(now,nex,count)
        if now < nex:
            now = nex
            continue
        s1 = str(now)
        s2 = str(nex)

        c1 = s1[:len(s2)]
        #print(c1)
        if int(c1) > int(s2):
            count += (len(s1)-len(s2)+1)
            s2 += "0"*(len(s1)-len(s2)+1)
            
            now = int(s2)
            continue
        if int(c1) < int(s2):
            count += len(s1)-len(s2)
            s2 += "0"*(len(s1)-len(s2))
            
            now = int(s2)
            #print(now)
            continue
        c2 = s1[len(s2):]
        
        if c2 != "9"*len(c2):
            c3 = int(c2)+1
            s3 = str(c3)
            if len(s3) < len(c2):
                s3 = "0"*(len(c2)-len(s3))+s3
            s2 += s3
            count += len(c2)
            now = int(s2)
            continue
        count += (len(s1)-len(s2)+1)
        s2 += "0"*(len(s1)-len(s2)+1)
        
        now = int(s2)
        #print(now)
    #print(now)
    return count



T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1,ans))