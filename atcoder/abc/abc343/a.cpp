#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a,b;
    cin >> a >> b;
    int s = a+b;
    for (int i = 0; i < 10; i++){
        if (i != s){
            cout << i << endl;
            return 0;
        }
    }


    return 0;
}
