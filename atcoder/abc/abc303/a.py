n = int(input())
S = input()
T = input()
for s,t in zip(S,T):
    if s == t:
        continue

    if (s,t) == ("1","l") or (t,s) == ("1","l"):
        continue

    if (s,t) == ("0","o") or (t,s) == ("0","o"):
        continue
    print("No")
    exit()
print("Yes")