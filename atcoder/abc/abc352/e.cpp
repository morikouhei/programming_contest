#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;
    dsu uf(n);
    vector<vector<int>> A(m);
    vector<int> K(m);
    vector<long long> C(m);
    vector<int> ind(m);
    for (int i = 0; i < m; i++){
        ind[i] = i;
        cin >> K[i] >> C[i];
        for (int j = 0; j < K[i]; j++){
            int a;
            cin >> a;
            a--;
            A[i].push_back(a);
        }
    }

    sort(ind.begin(),ind.end(),[&](int i, int j){
        return C[i] < C[j];
    });

    long long ans = 0;
    for (int i = 0; i < m; i++){
        long long c = C[ind[i]];
        set<int> s;
        for (auto a : A[ind[i]]){
            s.insert(uf.leader(a));
        }
        ans += c * (s.size()-1);
        int top = *s.begin();
        for (auto x : s){
            
            uf.merge(x,top);
        }
    }
    if (uf.size(0) != n){
        ans = -1;
    }
    cout << ans << endl;


    return 0;
}
