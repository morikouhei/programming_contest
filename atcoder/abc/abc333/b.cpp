#include <bits/stdc++.h>

using namespace std;
int main() {

    int S1,S2,T1,T2;

    char s;
    cin >> s;
    S1 = s - 'A';
    cin >> s;
    S2 = s - 'A';
    cin >> s;
    T1 = s-'A';
    cin >> s;
    T2 = s-'A';

    int d1,d2;
    d1 = abs(S1-S2);
    d2 = abs(T1-T2);

    d1 = min(d1,5-d1);
    d2 = min(d2,5-d2);

    if (d1 == d2) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}