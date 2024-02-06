n = int(input())
S = input()

maxs = [0]*27

now = [-1]
for s in S:
    ind = ord(s) - ord("a")
    if now[-1] == ind:
        now.append(ind)
        maxs[ind] = max(maxs[ind],len(now))
    else:
        i = now[-1]
        maxs[i] = max(maxs[i],len(now))
        now = [ind]
        maxs[ind] = max(maxs[ind],len(now))

ans = sum(maxs[:-1]) 
print(ans)       