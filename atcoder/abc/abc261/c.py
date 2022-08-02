n = int(input())
S = [input() for i in range(n)]

dic = {}
for s in S:
    if s in dic:
        num = dic[s]
        print(s+"("+str(num)+")")
    else:
        print(s)
    dic[s] = dic.get(s,0)+1
    