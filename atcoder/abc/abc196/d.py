import sys
sys.setrecursionlimit(3*10**5)
h,w,a,b = map(int,input().split())
ans = 0

def dfs(num,i,x,y):
    if i == h*w:
        return 1

    count = 0
    if num >> i & 1:
        return dfs(num,i+1,x,y)

    if y:
        count += dfs(num | 1<<i, i+1, x, y-1)
    if x:
        if (i%w) != w-1 and not (num >> (i+1) & 1): 
            count += dfs(num | 1 << i | 1<<(i+1),i+1,x-1,y)
        if i//w != h-1 and not (num >> (i+w) & 1): 
            count += dfs(num | 1 << i | 1<<(i+w),i+1,x-1,y)
    return count

print(dfs(0,0,a,b))
