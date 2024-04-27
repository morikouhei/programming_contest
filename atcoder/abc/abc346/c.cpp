#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    cin >> n >> k;
    long long ans = k * (k+1) / 2;
    set<long long> A;
    for (int i = 0; i < n; i++){
        long long a;
        cin >> a;
        A.insert(a);
    }

    for (auto a: A){
        if (a <= k){
            ans -= a;
        }
    }
    cout << ans << endl;


    return 0;
}
