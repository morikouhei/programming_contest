t = int(input())
for _ in range(t):
    s = input()+"0"
    l = []
    c = 0
    for i in s:
        if i == "1":
            c += 1
        else:
            if c > 0:
                l.append(c)
            c = 0
    l.sort(reverse=True)
    
    print(sum(l[0:len(l):2]))