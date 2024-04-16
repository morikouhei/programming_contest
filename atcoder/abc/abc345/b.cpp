#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long X;
    cin >> X;
    if (X >= 0){
        cout << (X+9)/10 << endl;
    } else{
        cout << X/10 << endl;
    }

    return 0;
}
