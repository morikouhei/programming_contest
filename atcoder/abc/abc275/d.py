import sys
sys.setrecursionlimit(3*10**5)
n = int(input())

dic = {}
dic[0] = 1

def f(x):
    if x in dic:
        return dic[x]

    cal = f(x//2)+f(x//3)
    dic[x] = cal
    return cal

print(f(n))