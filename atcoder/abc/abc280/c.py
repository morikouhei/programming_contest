S = input()
T = input()

for i,(s,t) in enumerate(zip(S,T)):
    if s != t:
        print(i+1)
        exit()
print(len(T))