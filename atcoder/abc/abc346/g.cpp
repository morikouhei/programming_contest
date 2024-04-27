#include <bits/stdc++.h>
using namespace std;

#include <atcoder/all>
using namespace atcoder;

const int INF = 1e6;
struct S {
    int mi,num;
};
using F = int;

S op(S l, S r){
    int mi = min(l.mi,r.mi);
    int num = 0;
    if (l.mi == mi) num += l.num;
    if (r.mi == mi) num += r.num;
    return S{mi,num};
}

S e() { return S{0, 0}; }

S mapping(F l, S r) { return S{l + r.mi, r.num}; }

F composition(F l, F r) { return l+r; }

F id() { return 0; }

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for (auto &a: A) cin >> a;
    vector<vector<int>> pos(n);
    vector<int> ind(n);
    for (int i = 0; i < n; i++){
        pos[A[i]-1].push_back(i);
    }
    for (int i = 0; i < n; i++){
        pos[i].push_back(n);
    }

    lazy_segtree<S, op, e, F, mapping, composition, id> seg(n);

    for (int i = 0; i < n; i++){
        seg.set(i,S{0,1});
    }
    for (int i = 0; i < n; i++){
        int a = i;
        if (ind[a] + 1 == pos[a].size()) continue;
        int l = pos[a][ind[a]], r = pos[a][ind[a]+1];
        seg.apply(l,r,1);
    }


    long long ans = 0;
    for (int i = 0; i < n; i++){
        S cand = seg.prod(i,n);
        if (cand.mi != 0) ans += (n-i);
        else ans += n-i - cand.num;

        int a = A[i]-1;
        seg.apply(pos[a][ind[a]],pos[a][ind[a]+1],-1);

        ind[a]++;

        if (ind[a] + 1 == pos[a].size()) continue;
        int l = pos[a][ind[a]], r = pos[a][ind[a]+1];
        seg.apply(l,r,1);
        
    }

    cout << ans << endl;


    return 0;
}
