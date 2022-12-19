k = int(input())

divs = {}
for i in range(2,int(k**0.5)+1):
    if k%i:
        continue
    num = 0
    while k%i == 0:
        k //= i
        num += 1
    divs[i] = num

if k != 1:
    divs[k] = 1


size = len(divs)

ans = 0

for div,num in divs.items():

    count = 0
    for i in range(1,50):
        x = div*i
        while x%div == 0:
            num -= 1
            x //= div
        if num <= 0:
            ans = max(ans,div*i)
            break
print(ans)