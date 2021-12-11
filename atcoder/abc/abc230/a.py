n = int(input())
if n > 41:
    n += 1
   
ans = "AGC"+"0"*(3-len(str(n)))+str(n)
print(ans)