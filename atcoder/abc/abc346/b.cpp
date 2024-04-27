#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S = "wbwbwwbwbwbw";
    int n = S.length();

    int w,b;
    cin >> w >> b;

    for (int i = 0; i < n; i++){
        int nw = 0, nb = 0;
        for (int j = 0; j < w+b;j++){
            if (S[(i+j)%n] == 'w') nw++;
            else nb++;
        }

        if (w == nw && b == nb){
            cout << "Yes" << endl;
            exit(0);
        }
    }

    cout << "No" << endl;

    return 0;
}
