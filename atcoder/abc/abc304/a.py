n = int(input())
SA = []
mi = 10**10
ind = -1
for i in range(n):
  s,a = input().split()
  a = int(a)
  if mi > a:
    mi = a
    ind = i
  SA.append(s)
  
for i in range(n):
  print(SA[(ind+i)%n])
  