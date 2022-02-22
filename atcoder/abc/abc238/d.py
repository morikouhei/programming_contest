def solve():
    a,s = map(int,input().split())
    if s >= 2*a:
    	return "No" if (s-2*a)&a else "Yes"
    return "No"

t = int(input())
for _ in range(t):
    print(solve())