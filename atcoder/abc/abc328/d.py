S = input()

q = ["#","#"]
for s in S:
    if s != "C":
        q.append(s)
        continue
    if q[-2] == "A" and q[-1] == "B":
        q.pop()
        q.pop()
    else:
        q.append(s)

print("".join(q[2:]))