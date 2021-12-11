S = input()
n = len(S)
K = int(input())
L = [i for i,s in enumerate(S) if s == "Y"]
L = [l-i for i,l in enumerate(L)]
accum = [0]
for i in range(len(L)):
    accum.append(accum[-1]+L[i])

def search(x):
    for i in range(len(L)-x+1):
        center = L[i+(x-1)//2]
        count = center*((x+1)//2) - (accum[i+(x+1)//2] - accum[i]) + (accum[i+x]-accum[i+(x+1)//2]) - center*(x//2)
        if count <= K:
            return 1
    return 0



l = 0
r = n+1

while r > l + 1:
    m = (r+l)//2
    
    if search(m):
        l = m

    else:
        r = m
print(l)
