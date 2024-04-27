#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;
    int num = 0;
    for (int i = 3; i < 6; i++){
        num *= 10;
        num += S[i]-'0';
    }

    if (num == 0 || num == 316 || num > 349){
        cout << "No" << endl;
    } else{
        cout << "Yes" << endl;
    }

    return 0;
}
