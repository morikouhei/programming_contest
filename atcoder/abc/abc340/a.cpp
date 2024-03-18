#include <bits/stdc++.h>
using namespace std;
int main()

{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, d;
    cin >> a >> b >> d;
    for (int i = a; i <= b; i += d)
    {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
