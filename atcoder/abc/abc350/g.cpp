#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const long long mod = 998244353;
    int n,q;
    cin >> n >> q;
    

    long long x = 0;
    for (int i = 0; i < q; i++){
        long long a,b,c;
        cin >> a >> b >> c;

        a = ((a*(1+x))%mod)%2;
        b = ((b*(1+x))%mod)%n;
        c = ((c*(1+x))%mod)%n;

        if (a == 0){
            add(b,c);
            add(c,b);
            continue;
        }

        long long x = (long long)get(b,c);
        cout << x << endl;

    }

    return 0;
}
