import random
n = 20
def size(x):
    return x*(x-1)//2


alls = set()

s = size(n)
print(s)
# for i in range(1<<s):

#     count = [0]*n
#     now = 0
#     for j in range(n):
#         for k in range(j+1,n):
#             if i >> now & 1:
#                 count[j] += 1
#                 count[k] += 1
#             now += 1
#     alls.add("".join([str(x) for x in sorted(count)]))
# alls.add("0"*n)
# alls.add("1"*n)
for i in range(0,101):
    
    
    for num in range(1000):
        line = []
        for j in range(s):
            if random.randint(1,100) <= i:
                line.append(1)
            else:
                line.append(0)

        count = [0]*n
        now = 0
        for j in range(n):
            for k in range(j+1,n):
                if line[now]:
                    count[j] += 1
                    count[k] += 1
                now += 1
        alls.add("_".join([str(x) for x in sorted(count)]))

alls = sorted(alls)
m = 100
dis = len(alls)//m
cand = []
for i in range(m):
    x = alls[i*dis]
    l = [int(j) for j in x.split("_")]
    cand.append(l)

for i in range(10):
    print(cand[i])
# print(len(alls))