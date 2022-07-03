from math import gcd
n,a,b = map(int,input().split())

def calc(x):
    return x*(x+1)//2
l = a*b//(gcd(a,b))

numa = a*calc(n//a)
numb = b*calc(n//b)
numl = l*calc(n//l)
print(calc(n)-numa-numb+numl)
