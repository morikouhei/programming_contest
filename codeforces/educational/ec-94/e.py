from sys import stdin
 
def input():
    return stdin.readline().strip()
n = int(input())
a = list(map(int,input().split()))

def bootstrap(f, stack=[]):
    from types import GeneratorType
 
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
res = 0

@bootstrap
def dfs(l,r,base):
    if r-l < 0:
        yield 0
    if r == l:
        yield 1 
    mn = min(a[l:r+1])
    count = r-l+1
    now = mn-base
    k = l
    for i in range(l,r+1):
        if a[i] == mn:
            now += yield dfs(k,i-1,mn)
            k = i+1
    now += yield dfs(k,r,mn)
    yield min(count,now)
if sum(a) == 0:
    print(0)
else:
    print(dfs(0,n-1,0))