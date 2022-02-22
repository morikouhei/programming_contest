n = int(input())

a = n**2
b = 1
count = 0
while count < n and b <= a:
    b *= 2
    count += 1
if b > a:
    print("Yes")
else:
    print("No")