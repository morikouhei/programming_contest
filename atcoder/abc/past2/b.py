s = input()
a = s.count("a")
b = s.count("b")
c = s.count("c")
if max(a,b,c) == a:
    print("a")
elif max(a,b,c) == b:
    print("b")
else:
    print("c")