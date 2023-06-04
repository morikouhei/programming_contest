n = int(input())
S = input()
t = S.count("T")
a = n-t

if t != a:
    print("T" if t > a else "A")
else:
    print("T" if S[-1] == "A" else "A")