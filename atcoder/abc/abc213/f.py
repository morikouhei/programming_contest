from collections import Counter, deque

### Suffix Array algorithm: you have to pass string(s) ###

def sa_naive(s):
    n = len(s)
    sa = list(range(n))
    sa.sort(key=lambda x: s[x:])
    return sa

def sa_doubling(s):
    n = len(s)
    sa = list(range(n))
    rnk = s
    tmp = [0]*n
    k = 1
    while k < n:
        sa.sort(key=lambda x: (rnk[x],rnk[x+k]) if x+k < n else (rnk[x],-1))
        tmp[sa[0]] = 0
        for i in range(1,n):
            tmp[sa[i]] = tmp[sa[i-1]]
            if sa[i-1] + k < n:
                x = (rnk[sa[i-1]], rnk[sa[i-1]+k])
            else:
                x = (rnk[sa[i-1]],-1)
            if sa[i] + k < n:
                y = (rnk[sa[i]], rnk[sa[i]+k])
            else:
                y = (rnk[sa[i]],-1)

            if x < y:
                tmp[sa[i]] += 1
        k *= 2
        tmp,rnk = rnk,tmp

    return sa


def sa_is(s,upper):
    n = len(s)
    if n == 0:
        return []
    if n == 1:
        return[0]
    if n == 2:
        if s[0] < s[1]:
            return [0,1]
        else:
            return [1,0]
    if n < 10:
        return sa_naive(s)
    if n < 40:
        return sa_doubling(s)

    ls = [0]*n
    for i in range(n-2,-1,-1):
        ls[i] = ls[i+1] if s[i] == s[i+1] else s[i] < s[i+1]
    sum_l = [0]*(upper+1)
    sum_s = [0]*(upper+1)
    for i in range(n):
        if ls[i]:
            sum_l[s[i]+1] += 1
        else:
            sum_s[s[i]] += 1
    for i in range(upper):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i+1] += sum_s[i]

    lms_map = [-1]*(n+1)
    lms = []
    m = 0
    for i in range(1,n):
        if not ls[i-1] and ls[i]:
            lms_map[i] = m
            lms.append(i)
            m += 1
    
    sa = [-1]*n
    buf = sum_s.copy()
    for d in lms:
        if d == n:
            continue
        sa[buf[s[d]]] = d
        buf[s[d]] += 1
    buf = sum_l.copy()
    sa[buf[s[n-1]]] = n-1
    buf[s[n-1]] += 1
    for i in range(n):
        v = sa[i]
        if v >= 1 and not ls[v-1]:
            sa[buf[s[v-1]]] = v-1
            buf[s[v-1]] += 1
    buf = sum_l.copy()
    for i in range(n)[::-1]:
        v = sa[i]
        if v >= 1 and ls[v-1]:
            buf[s[v-1]+1] -= 1
            sa[buf[s[v-1]+1]] = v-1
    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0]*m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1,m):
            l = sorted_lms[i-1]
            r = sorted_lms[i]
            end_l = lms[lms_map[l]+1] if lms_map[l]+1 < m else n
            end_r = lms[lms_map[r]+1] if lms_map[r]+1 < m else n
            same = True
            if end_l -l != end_r - r:
                same = False
            else:
                while l < end_l:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r += 1
                if l == n or s[l] != s[r]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
        rec_sa = sa_is(rec_s,rec_upper)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]
        
        sa = [-1]*n
        buf = sum_s.copy()
        for d in sorted_lms:
            if d == n:
                continue
            sa[buf[s[d]]] = d
            buf[s[d]] += 1
        buf = sum_l.copy()
        sa[buf[s[n-1]]] = n-1
        buf[s[n-1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v-1]:
                sa[buf[s[v-1]]] = v-1
                buf[s[v-1]] += 1
        buf = sum_l.copy()
        for i in range(n)[::-1]:
            v = sa[i]
            if v >= 1 and ls[v-1]:
                buf[s[v-1]+1] -= 1
                sa[buf[s[v-1]+1]] = v-1

    return sa


def suffix_array(s,upper=255):
    if type(s) is str:
        s = [ord(c) for c in s]
    return sa_is(s,upper)

def lcp_array(s,sa):
    n = len(s)
    rnk = [0]*n
    for i in range(n):
        rnk[sa[i]] = i
    lcp = [0]*(n-1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i]-1]
        while j + h < n and i + h < n:
            if s[j+h] != s[i+h]:
                break
            h += 1
        lcp[rnk[i]-1] = h
    return lcp

n = int(input())
S = input()
sa = suffix_array(S)
lcp = lcp_array(S,sa)

ans = [n-i for i in range(n)]
for _ in range(2):
    q = deque([])
    count = 0
    for i,l in enumerate(lcp):
        size = 1
        while q and q[-1][0] >= l:
            count -= q[-1][0]*q[-1][1]
            size += q[-1][1]
            q.pop()
        count += size*l
        q.append([l,size])
        ans[sa[i+1]] += count
    sa = sa[::-1]
    lcp = lcp[::-1]
for i in ans:
    print(i)