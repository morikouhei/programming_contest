n,m,x,t,d = map(int,input().split())

s = t - d*x
# print(s)
for i in range(min(m,x)):
    s += d
print(s)