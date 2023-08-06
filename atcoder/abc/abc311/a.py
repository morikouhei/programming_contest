n = int(input())
S = input()
abc = set()
for i,s in enumerate(S):
    abc.add(s)
    if len(abc) == 3:
        print(i+1)
        exit()