#include <bits/stdc++.h>
using namespace std;

#include <atcoder/all>
using namespace atcoder;

long long nc2(long long n){

    return n * (n-1) / 2;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;
    dsu uf(n);
    vector<pair<int,int>> edges;
    for (int i = 0; i < m; i++){
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        uf.merge(a,b);
        edges.push_back({a,b});
    }

    vector<int> count(n);
    for (auto [a,b]: edges){
        count[uf.leader(a)]++;
    }
    long long ans = 0;
    for (int i = 0; i < n; i++){
        if (uf.leader(i) != i) continue;
        ans += nc2((long long)uf.size(i)) - count[i];
    }
    cout << ans << endl;

    

    return 0;
}
