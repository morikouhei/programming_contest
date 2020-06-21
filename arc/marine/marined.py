a,b = input().split()
ans = 0
if int(a[0]) < 9:
    ans = int(a)+(9-int(a[0]))*100 -int(b)
elif int(a[1]) < 9:
    ans = int(a)+(9-int(a[1]))*10 -int(b)
else:
    ans = int(a)+(9-int(a[2])) -int(b)

if int(b[0]) > 1:
    ans2 = int(a)+(int(b[0])-1)*100 -int(b)
elif int(b[1]) > 0:
    ans2 = int(a)+(int(b[1]))*10 -int(b)
else:
    ans2 = int(a)+(int(b[2])) -int(b)
print(max(ans,ans2))