#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

using mint = modint998244353;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    scc_graph scc(n);
    vector<int> A(n);
    for (int i = 0 ; i < n; i++){
        int a;
        cin >> a;
        a--;
        A[i] = a;
        scc.add_edge(i,a);
    }

    auto group = scc.scc();

    vector<int> count(n);

    long long ans = 0;

    for (auto g: group){
        long long s = g.size();

        ans += s * s;
        int base = 0;
        for (auto i: g){
            base += count[i];
        }
        for (auto i: g){
            ans += base;
            count[A[i]] += base + s;
        }
    }

    cout << ans << endl;
    

    
}
