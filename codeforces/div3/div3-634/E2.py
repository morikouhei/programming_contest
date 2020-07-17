### 尺取りよりも累積和的なリストを持ったほうが早かった　リスト一列のコピーも早そう

from sys import stdin

def input():
   return stdin.buffer.readline()

def main():   
    
    def solve():
        n = int(input())
        l = list(map(int,input().split()))
        sl = [[] for i in range(201)]
        ss = [[0]*201]
        
        for i in range(n):
            sl[l[i]].append(i)    
            ss.append(ss[-1].copy())
            
            ss[-1][l[i]] += 1
    
        ans = 0
        for i in range(1,201):
            if not sl[i]:
                continue
            if len(sl[i]) == 1:
                ans = max(ans,1)
                continue
            for j in range(len(sl[i])//2):
                le = sl[i][j]
                ri = sl[i][-1-j]
                for k in range(1,201):
                    if i == k:
                        ans = max(ans,len(sl[i]))
                        continue
                    if sl[k]:
                        ans = max(ans,2*(j+1)+ss[ri][k]-ss[le][k])
                    
        print(ans)

    t = int(input())
    for q in range(t):
        solve()

if __name__ == "__main__":
    main()
    
