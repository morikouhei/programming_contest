import itertools
k = int(input())

ans = []
for i in range(1,11):

    for l in itertools.combinations(range(10),i):
        l = list(l)
        l.sort(reverse=True)
        
        num = 0
        for d in l:
            num *= 10
            num += d
        ans.append(num)

ans.sort()
print(ans[k])