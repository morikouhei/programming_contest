S = input()

count = [0]*26

q = []
for s in S:
    if s == "(":
        q.append(s)
        continue

    if "a" <= s <= "z":
        o = ord(s)-ord("a")
        q.append(o)
        

        if count[o]:
            print("No")
            exit()
        count[o] += 1

        continue

    while q:
        if q[-1] == "(":
            q.pop()
            break
        count[q.pop()] -= 1
    
print("Yes")
