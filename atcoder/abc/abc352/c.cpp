#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    long long ma = 0,sum = 0;
    for (int i = 0; i < n; i++){
        long long a,b;
        cin >> a >> b;
        sum += a;
        ma = max(ma,b-a);
    }
    cout << ma + sum << endl;

    return 0;
}
