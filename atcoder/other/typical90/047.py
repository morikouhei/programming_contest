n = int(input())
S = input()
T = input()
dic = {"R":0, "G":1, "B":2}
S = [dic[s] for s in S]
T = [dic[t] for t in T]
mod = 699999953

ans = 0
for i in range(3):
    seq = [(i-t)%3 for t in T]
    pow3 = 1
    hashs = 0
    hasht = 0
    for j in range(n):
        hashs = (hashs*3 + S[j])%mod
        hasht = (hasht+ pow3*seq[n-j-1])%mod
        if hashs == hasht:
            ans += 1
        pow3 = (pow3*3)%mod

    pow3 = 1
    hashs = 0
    hasht = 0
    for j in range(n-1):
        hashs = (hashs + pow3*S[n-j-1])%mod
        hasht = (hasht*3 + seq[j])%mod
        if hashs == hasht:
            ans += 1
        pow3 = (pow3*3)%mod
print(ans)