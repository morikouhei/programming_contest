#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int h;
    cin >> h;
    for (int i = 2; i <= n; i++){
        int x;
        cin >> x;
        if (h < x){
            cout << i << endl;
            return 0;
        }
    }
    cout << -1;
    
    return 0;
}
