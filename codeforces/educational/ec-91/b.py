t = int(input())
for _ in range(t):
    s = input()
    R = s.count("R")
    P = s.count("P")
    S = s.count("S")
    x = max(R,P,S)
    if x == R:
        print("P"*len(s))
    elif x == P:
        print("S"*len(s))
    else:
        print("R"*len(s))