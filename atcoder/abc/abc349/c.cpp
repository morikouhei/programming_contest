#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S,T;
    cin >> S >> T;
    int num = 0;
    for (char s: S){
        if (num < 3 && toupper(s) == T[num]){
            num++;
        }
    }
    cout << (num >= 2 ? "Yes" : "No") << endl;

    return 0;
}
