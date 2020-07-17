s = input()

d = set()
for i in range(len(s)):
    now = ""
    for j in range(i,i+3):
        if j >= len(s):
            break
        now += s[j]
    
    if len(now) == 1:
        d.add(now)
        d.add(".")
    elif len(now) == 2:
        d.add(now[0])
        d.add(".")
        d.add(now[1])
        d.add(now)
        d.add("..")
        k = now[0]+"."
        d.add(k)
        k = "."+now[1]
        d.add(k)
    else:
        d.add(now[0])
        d.add(".")
        d.add(now[1])
        d.add(now[2])
        d.add(now[:2])
        d.add(now[1:])
        d.add("..")
        k = now[0]+"."
        d.add(k)
        k = "."+now[1]
        d.add(k)
        d.add(now[1]+".")
        d.add("."+now[2])
        d.add("...")
        d.add(now[:2]+".")
        d.add(now[0]+"."+now[2])
        d.add("."+now[1:])
        d.add(now)
        d.add(".."+now[2])
        d.add(now[0]+"..")
        d.add("."+now[1]+".")
print(len(d))


