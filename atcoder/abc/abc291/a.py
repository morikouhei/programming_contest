S = input()
for i,s in enumerate(S,1):
    if s.upper() == s:
        print(i)
        exit()