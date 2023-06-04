from bisect import bisect_left 

w,h = map(int,input().split())
n = int(input())
PQ = [list(map(int,input().split())) for i in range(n)]
a = int(input())
A = list(map(int,input().split())) + [w]
b = int(input())
B = list(map(int,input().split())) + [h]

dic = {}

for p,q in PQ:
  x = bisect_left(A,p)
  y = bisect_left(B,q)
  if (x,y) not in dic:
    dic[(x,y)] = 0
  dic[(x,y)] += 1
vs = sorted([v for v in dic.values()])
if len(dic) == (a+1)*(b+1):
  m = vs[0]
else:
  m = 0

M = vs[-1]
print(m,M)