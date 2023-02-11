S = input()
T = input()
n = len(S)
front = [0]*(n+1)
back = [0]*(n+1)
front[0] = 1
back[0] = 1
for i,(s,t) in enumerate(zip(S,T),1):
    if s == t or s == "?" or t == "?":
        front[i] = 1
    else:
        break

for i,(s,t) in enumerate(zip(S[::-1],T[::-1]),1):
    if s == t or s == "?" or t == "?":
        back[i] = 1
    else:
        break
lT = len(T)
for i in range(lT+1):
    if front[i] and back[lT-i]:
        print("Yes")
    else:
        print("No")