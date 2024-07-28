#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,x,y,z;
    cin >> n >> x >> y >> z;

    cout << (min(x,y) < z && max(x,y) > z ? "Yes": "No") << endl;

    return 0;
}
