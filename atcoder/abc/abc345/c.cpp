#include <bits/stdc++.h>
using namespace std;

long long solve(string S){
    long long n = S.length();
    vector<long long> count(26);
    for (auto& s: S){
        count[s-'a']++;
    }

    int same = 0;

    long long ans = n * (n-1) / 2;

    for (auto& s: S){
        count[s-'a']--;
        if (count[s-'a']) same = 1;
        ans -= count[s-'a'];
    }
    return ans + same;

}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S;
    cin >> S;

    cout << solve(S) << endl;
    

    return 0;
}
