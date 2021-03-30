t = int(input())
for _ in range(t):
    a = input()
    b = input()
    ans = len(a)+len(b)
    for i in range(len(a)):
        for j in range(i,len(a)):
            for k in range(len(b)):
                for x in range(k,len(b)):
                    if a[i:j+1] == b[k:x+1]:
                        ans = min(ans,i+len(a)-j-1+k+len(b)-1-x)
    print(ans)