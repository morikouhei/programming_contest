#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

using mint = modint998244353;

struct S {
    mint a, b, ab;
    int size;

};

struct F {
    mint a, b;
};

S op(S l, S r) { 

    return S{l.a + r.a, l.b+r.b, l.ab+r.ab, l.size + r.size}; }

S e() { return S{0, 0, 0, 0}; }

S mapping(F l, S r) { return S{l.a*r.size+r.a,l.b*r.size+r.b,r.ab+l.a*r.b+l.b*r.a + l.a*l.b*r.size, r.size}; }

F composition(F l, F r) { return F{r.a + l.a, r.b + l.b}; }

F id() { return F{0, 0}; }

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,q;
    cin >> n >> q;
    vector<long long> A(n);
    vector<long long> B(n);
    for (auto &a: A) cin >> a;
    for (auto &b: B) cin >> b;

    lazy_segtree<S, op, e, F, mapping, composition, id> seg(n);
    for (int i = 0; i < n; i++){
        seg.set(i,S{A[i],B[i],A[i]*B[i],1});
    }
    
    for (int i = 0; i < q; i++){
        int t,l,r;
        cin >> t >> l >> r;
        l--;
        if (t == 1 || t == 2){
            long long x;
            cin >> x;
            if (t == 1){
                seg.apply(l,r,F{x,0});
            }
            else {
                seg.apply(l,r,F{0,x});
            }
        }

        if (t == 3){
            auto ans = seg.prod(l,r);
            cout << ans.ab.val() << endl;
        }
    }

    
}
