n = int(input())
s = [list(input()) for i in range(n)]
M = 10**6+5
child = [[0]*26]
is_end = [0]*M
l = []
now = 1
def stoi(a):
    return ord(a)-ord("a")
for i in s:
    si = i[::-1]
    suf = []
    node = 0
    for j in si:
        suf.append(node)
        if child[node][stoi(j)] == 0:
            child.append([0]*26)
            child[node][stoi(j)] = now
            now += 1
        node = child[node][stoi(j)]
    is_end[node] += 1
    l.append(suf)

ans = 0
for i in range(n):
    li = l[i][::-1]
    si = s[i]
    suf = set()
    for j in range(len(si)):
        suf.add(si[j])
        if j == 0:
            continue
        node = li[j]
        for c in suf:
            ans += is_end[child[node][stoi(c)]]
print(ans)
