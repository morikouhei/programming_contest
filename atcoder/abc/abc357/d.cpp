#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;

using mint = modint998244353;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    cin >> n;

    int le = 0;
    long long temp = n;
    mint ten = 1;
    while (temp){
        ten *= 10;
        temp /= 10;
    }

    mint ans = n * (ten.pow(n)-1) / (ten-1);
    cout << ans.val() << endl;

    
    
    return 0;
}
