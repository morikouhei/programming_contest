#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,k;
    cin >> n >> k;
    vector<int> P(n);
    for (auto &p: P) cin >> p;

    vector<int> ind(n);
    for (int i = 0; i < n; i++){
        ind[i] = i;
    }
    sort(ind.begin(),ind.end(), [&](int i, int j){
        return P[i] > P[j];
    });
    set<int> s;
    int ans = n+1;
    for (int i = 0; i < n; i++){
        int p = ind[i];
        s.insert(p);
        if (i >= k-1){
            ans = min(ans,*s.rbegin()-*s.begin());
            s.erase(ind[i-k+1]);
        }
    }
    cout << ans << endl;


    return 0;
}
