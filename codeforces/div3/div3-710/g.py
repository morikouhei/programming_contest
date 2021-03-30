t = int(input())
for _ in range(t):
    S = input()
    l = [[] for i in range(26)]
    for i in range(len(S))[::-1]:
        l[ord(S[i])-ord("a")].append(i)

    ans = ""
    now = -1
    while True:
        nex = 10**10
        ind = -1
        for i in range(26):
            if l[i] and nex > l[i][0]:
                nex = l[i][0]
                ind = i
        if ind == -1:
            break

        for i in range(26)[::-1]:

            while l[i] and l[i][-1] <= now:
                l[i].pop()
            if l[i] and l[i][-1] <= nex:
                ans += chr(ord("a")+i)
                now = l[i][-1]
                l[i] = []
                break

    print(ans)

