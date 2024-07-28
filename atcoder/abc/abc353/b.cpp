#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,k;
    cin >> n >> k;
    int ans = 1;
    int now = k;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        if (a > now){
            ans++;
            now = k;
        }
        now -= a;
    }
    cout << ans << endl;
    
    return 0;
}
