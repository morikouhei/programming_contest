#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l,r;
    cin >> l >> r;
    vector<pair<long long, long long>> ans;
    
    auto dfs = [&](auto dfs, long long nl, long long nr) -> void {
        if (l <= nl && nr <= r){
            ans.push_back({nl,nr});
            return ;
        }
        if (r <= nl) return ;
        if (nr <= l) return ;
        dfs(dfs,nl,(nr+nl)/2);
        dfs(dfs,(nr+nl)/2,nr);

    };
    dfs(dfs,0,1ll<<61);
    sort(ans.begin(),ans.end());
    cout << ans.size() << endl;
    for (auto [f,s] : ans){
        cout << f << " " << s << endl;
    }

    return 0;
}
