n = int(input())
S = [input() for i in range(n)]
if len(set(S)) != n:
    print("No")
    exit()

for s in S:
    if len(s) != 2:
        print("No")
        exit()
    s = list(s)
    if s[0] not in "HDCS":
        print("No")
        exit()
    if s[1] not in "A23456789TJQK":
        print("No")
        exit()
print("Yes")