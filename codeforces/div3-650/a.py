t = int(input())
for _  in range(t):
    s = input()
    a = ""
    for i in range(0,len(s)-2,2):
        a += s[i]
    a += s[-2]
    a += s[-1]
    print(a)