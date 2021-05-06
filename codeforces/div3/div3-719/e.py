t = int(input())
for _ in range(t):
    n = int(input())
    S = input()
    count = 0
    ans = [0]*n
    now = 0
    cum = 0
    for i in range(n):
        if S[i] == "*":
            count += 1

    for i in range(n):
        if S[i] == "*":
            need = now*(now+1)//2
            ans[i] += cum -need
            now += 1
            
        else:
            need = now*(now+1)//2
            ans[i] += cum -need
        cum += now
    
    now = 0
    cum = 0
    for i in range(n)[::-1]:
        if S[i] == "*":
            need = now*(now+1)//2
            ans[i] += cum -need
            now += 1
            
        else:
            need = now*(now+1)//2
            ans[i] += cum -need
            if now == 0 or now == count:
                ans[i] += count
            else:
                ans[i] += min(count-now,now)
        cum += now
    print(min(ans))