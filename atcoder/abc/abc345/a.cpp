#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;

    int ok = 1;
    if (S[0] != '<') ok = 0;
    if (S[S.length()-1] != '>') ok = 0;
    for (int i = 1; i < S.length()-1;i++){
        if (S[i] != '=') ok = 0;
    }

    cout << (ok ? "Yes": "No") << endl;
    return 0;
}
