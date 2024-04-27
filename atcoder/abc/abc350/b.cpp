#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,q;
    cin >> n >> q;
    vector<int> state(n,1);

    for (int i = 0; i < q; i++){
        int t;
        cin >> t;
        t--;
        state[t]^= 1;
    }
    int ans = 0;
    for (int i = 0; i < n; i++){
        ans += state[i];
    }
    cout << ans << endl;

    return 0;
}
