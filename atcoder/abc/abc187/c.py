n = int(input())
from collections import defaultdict
dic1 = defaultdict(int)
dic2 = defaultdict(int)
for i in range(n):
    s = input()
    if s[0] == "!":
        dic1[s[1:]] += 1
    else:
        dic2[s]+= 1
for i in dic1.keys():
    if dic2[i] > 0:
        print(i)
        exit()
print("satisfiable")