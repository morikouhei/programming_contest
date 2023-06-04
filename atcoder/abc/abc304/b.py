n = int(input())
if n < 1000:
  print(n)
else:
  le = len(str(n))
  s = str(n)
  print(s[:3] + "0"*(le-3))