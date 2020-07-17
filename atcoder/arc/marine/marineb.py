a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
dif = abs(a-b)
if (v-w)*t >= dif:
    print("YES")
else:
    print("NO")