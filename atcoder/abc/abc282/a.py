k = int(input())
ans = [chr(ord("A")+i) for i in range(k)]
print(*ans,sep="")