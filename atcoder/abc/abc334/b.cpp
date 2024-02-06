#include<bits/stdc++.h>
// #include <atcoder/segtree>
// using namespace atcoder;
using namespace std;
// using mint=atcoder::modint998244353;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    long long A,M,L,R;
    cin >> A >> M >> L >> R;

    long long add = (long long)2e18/M*M;
    A += add;
    L += add;
    R += add;

    A %= M;
    L -= A;
    R -= A;
  
    
    long long ans = R/M - (L-1)/M;

    cout << ans << endl;
    return 0;

}
