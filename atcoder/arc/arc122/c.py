n = int(input())
fib = [1,1]
for i in range(86):
    fib.append(fib[-1]+fib[-2])

ans = []
for i in range(86,-1,-1):
    if n >= fib[i]:
        if i%2 == 0:
            ans.append(1)
        else:
            ans.append(2)
        n -= fib[i]
    if i%2 == 0:
        ans.append(4)
    else:
        ans.append(3)

if n:
    ans.append(1)

print(len(ans))
for i in ans:
    print(i)

