#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a,b,c;
    cin >> a >> b >> c;

    int bi = __builtin_popcountll(c);
    
    for (int i = 0; i <= bi; i++){
        if (a < i) continue;
        if (b < bi-i) continue;
        if (a-i != b - bi + i) continue;
        long long na = 0,nb = 0;
        int nbi = 0;
        int other = a-i;

        if (other > 60-bi) continue;

        for (int j = 0; j < 60; j++){
            if (c >> j & 1){
                if (nbi < i){
                    na |= 1ll<<j;
                } else{
                    nb |= 1ll<<j;
                }
                nbi++;
            } else{
                if (other){
                    na |= 1ll<<j;
                    nb |= 1ll<<j;
                    other--;
                }
            }
        }

        assert (__builtin_popcountll(na) == a);
        assert (__builtin_popcountll(nb) == b);

        cout << na << " " << nb << endl;
        exit(0);

    }

    cout << -1 << endl;





    return 0;
}
