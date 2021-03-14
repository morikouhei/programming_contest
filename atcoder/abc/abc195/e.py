import sys
sys.setrecursionlimit(10**6)
n = int(input())
S = input()
X = input()

dic = {}

def dfs(x,num):
    if (x,num) in dic:
        return dic[(x,num)]
    if x == n:
        if num%7:
            return 0
        else:
            return 1
    
    turn = 1 if X[x] == "T" else 0
    now = int(S[x])
    t = num*10%7
    win = 1
    if turn:
        if dfs(x+1,(t+now)%7) == 1 or dfs(x+1,t) == 1:
            win = 1
        else:
            win = 0
    else:
        if dfs(x+1,(t+now)%7) == 1 and dfs(x+1,t) == 1:
            win = 1
        else:
            win = 0
    
    dic[(x,num)] = win
    return win

win = dfs(0,0)
if win:
    print("Takahashi")
else:
    print("Aoki")