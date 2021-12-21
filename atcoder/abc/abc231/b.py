n = int(input())
dic = {}
for i in range(n):
    s = input()
    dic[s] = dic.get(s,0)+1

m = max(dic.values())
for k,v in dic.items():
    if v == m:
        print(k)
        