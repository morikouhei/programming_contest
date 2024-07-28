#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> A(n);
    for (auto &a: A) cin >> a;
    sort(A.begin(),A.end());

    long long ans = 0;
    for (auto a: A){
        ans += a * (n-1);
    }
    int now = n-1;
    for (int i = 0; i < n; i++){
        while (now > 0 && A[i]+A[now] >= (long long)1e8) now--;

        long long dif = n-max(i,now)-1;
        ans -= dif*1e8;

    }
    cout << ans << endl;
    
    return 0;
}
