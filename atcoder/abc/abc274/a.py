a,b = map(int,input().split())
b *= 10**4

if b == 0:
    print("0.000")
    exit()
ans = b//a
d = ans%10
ans //= 10
if d >= 5:
    ans += 1

out = []
while ans:
    out.append(ans%10)
    ans //= 10
out = out[::-1]
if len(out) == 3:
    out = [0,"."]+out
else:
    
    out.insert(1,".")
print(*out,sep="")