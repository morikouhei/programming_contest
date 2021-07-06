a,b,c,d = map(int,input().split())
if b >= d*c:
    print(-1)
else:
    need = (a+d*c-b-1)//(d*c-b)
    print(need)