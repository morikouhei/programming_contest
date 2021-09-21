x = list(input())
dic = {s:i for i,s in enumerate(x)}
n = int(input())
S = [input() for i in range(n)]
nS = []
add = []
for i in range(n):

    if len(S[i]) == 10:
        nS.append(S[i])
        continue
    nS.append(S[i]+x[0]*(10-len(S[i])))
count = []
for i,s in enumerate(nS):
    cal = 0
    for j in range(10):
        cal *= 26
        cal += dic[s[j]]
    count.append((cal,len(S[i]),i))
count.sort()

for i in range(n):
    print(S[count[i][2]])