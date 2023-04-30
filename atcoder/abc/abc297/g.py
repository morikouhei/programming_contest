n,l,r = map(int,input().split())
A = list(map(int,input().split()))

xor = 0

loop = l+r
for a in A:
    a %= loop
    xor ^= a//l

def greedy():
    xor = 0
    grandy = [0]*(max(A)+1)
    for i in range(l,len(grandy)):
        s = set()
        for j in range(l,r+1):
            if i-j >= 0:
                s.add(grandy[i-j])

        
        for j in range(30):
            if j not in s:
                grandy[i] = j
                break
        

    for a in A:
        xor ^= grandy[a]

    return "First" if xor else "Second"


ans = "First" if xor else "Second"

print(ans)