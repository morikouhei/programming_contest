S = list(input())
minans = S
maxans = S
for i in range(len(S)):
    S = S[1:]+S[:1]
    minans = min(minans,S)
    maxans = max(maxans,S)

print(*minans,sep="")
print(*maxans,sep="")