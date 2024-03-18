#include <bits/stdc++.h>
using namespace std;
int main()

{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> A(n);
    for (auto&a: A) cin >> a;
    for (int i = 0; i < n-1;i++){
        long long s,t;
        cin >> s >> t;
        A[i+1] += A[i]/s*t;
    }
    cout << A[n-1] << endl;
    return 0;
}
