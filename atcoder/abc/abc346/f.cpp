#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;
    string S,T;
    cin >> S >> T;
    int ns = S.length(), nt = T.length();

    vector<vector<int>> pos(26);
    for (int i = 0; i < ns; i++){
        pos[S[i]-'a'].push_back(i);
    }

    long long l = 0, r = (1e17)+5;

    auto calc = [&](long long m){
        long long now = 0;
        long long loop = 0;
        for (auto s: T){
            int p = s - 'a';
            if (pos[p].empty()) return false;
            long long nm = m;
            nm--;
            
            if (now >= ns){
                loop++;
                now %= ns;
            }

            int ind = lower_bound(pos[p].begin(),pos[p].end(),now) - pos[p].begin();
            
            if (pos[p].size()-ind > nm){
                now = pos[p][ind+nm]+1;
                continue;
            }

            loop++;
            nm -= pos[p].size()-ind;
            loop += nm/pos[p].size();
            if (loop > n) return false;
            nm %= (long long)pos[p].size();
            now = pos[p][nm]+1;

        }
        cout << "loop = " << loop << " n = " << n << endl;
        return (loop < n);
    };

    while (r-l > 1){
        cout << "l = " << l << " r = " << r << " m = " << (r+l)/2 << endl;
        long long m = (r+l)/2;
        if (calc(m)){
            l = m;
        } else{
            r = m;
        }
    }

    cout << l << endl;

    return 0;
}
