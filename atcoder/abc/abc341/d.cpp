#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n,m,k;
    cin >> n >> m >> k;

    long long lc = lcm(n,m);

    long long l = 0, r = 1e18;
    while (r > l + 1){
        long long c = (r+l)/2;

        long long num = c/n + c/m - c/lc * 2;
        if (num < k){
            l = c;
        } else {
            r = c;
        }
    }

    cout << r << endl;
    return 0;
}
