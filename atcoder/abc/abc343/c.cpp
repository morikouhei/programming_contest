#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;

    long long ans = 1;

    for (long long i = 1; i <= 1000010; i++){
        long long num = i * i * i;
        if (num > n) {
            break;
        }

        string s = to_string(num);

        int ok = 1;

        for (int j = 0; j < s.size();j++){
            if (s[j] != s[s.size()-1-j]) ok = 0;
        }
        if (ok) {
            ans = max(ans,num);
        }
    }


    cout << ans << endl;


    return 0;
}
