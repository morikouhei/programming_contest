from collections import Counter
n = int(input())
l = [input() for i in range(n)]
c = Counter(l)
for s in ["AC","WA","TLE","RE"]:
    if c[s]:
        print(s,"x",c[s])
    else:
        print(s,"x",0)