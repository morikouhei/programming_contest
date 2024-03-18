#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    string T = "";
    cin >> S;
    int count = 0;
    for (char c: S){
        if (c == '|'){
            count++;
        }
        else{
            if (count%2 == 0){
                T += c;
            }
        }
    }
    cout << T << endl;
    return 0;
}
