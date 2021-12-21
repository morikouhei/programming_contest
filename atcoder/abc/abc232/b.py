S = input()
T = input()

l = []
for s,t in zip(S,T):
    l.append((ord(s)-ord(t))%26)
if len(set(l)) == 1:
    print("Yes")
else:
    print("No")