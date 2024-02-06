
#include<bits/stdc++.h>
// #include <atcoder/segtree>
// using namespace atcoder;
using namespace std;
// using mint=atcoder::modint998244353;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int N,Q;
    cin >> N >> Q;
    vector<long long> R(N);
    for (int i = 0;i < N ;i++){
        cin >> R[i];
    }

    sort(R.begin(),R.end());
    vector<long long> cum(N+1);
    for (int i = 0; i < N ;i++){
        cum[i+1] = cum[i] + R[i];
    }

    while (Q--){
        long long X;
        cin >> X;

        int ans = upper_bound(cum.begin(),cum.end(),X) - cum.begin() - 1;
        cout << ans << endl;

    }
    return 0;

}
