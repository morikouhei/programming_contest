#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> pos(n+1);
    for (int i = 0; i < n; i++){
        int p;
        cin >> p;
        pos[p] = i;
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++){
        int a,b;
        cin >> a >> b;
        if (pos[a] > pos[b]){
            cout << b << endl;
        } else {
            cout << a << endl;
        }
    }
    return 0;
}
