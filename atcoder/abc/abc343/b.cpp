#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            int a;
            cin >> a;
            if (a == 0) continue;
            cout << j+1 << " ";
        }
        cout << endl;
    }


    return 0;
}
