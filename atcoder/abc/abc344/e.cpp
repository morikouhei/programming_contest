#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    map<int,int> s;
    vector<int> A(n);
    for (int i = 0; i < n; i++){
        cin >> A[i];
        s[A[i]] = 1;
    }

    int q;
    cin >> q;
    vector<array<int,3>> Q;

    for (int i = 0; i < q; i++){
        int t,x,y;
        cin >> t;
        if (t == 1){
            cin >> x >> y;
            s[y] = 1;
        }
        if (t == 2){
            cin >> x;
            s[x] = 1;
        }
        Q.push_back({t,x,y});
    }

    map<int,int> pos;
    map<int,int> rpos;
    int num = 0;
    for (auto [key,value] : s){
        pos[key] = num;
        rpos[num] = key;
        num++;
    }

    vector<int> L(num+1,-1);
    vector<int> R(num+1,-1);

    int top = pos[A[0]];

    for (int i = 0; i < n; i++){
        int p = pos[A[i]];
        assert (p >= 0);
        if (i > 0){
            L[p] = pos[A[i-1]];
        }
        if (i < n-1){
            R[p] = pos[A[i+1]];
        }
    }

    auto add = [&](int x, int y){
        int px = pos[x];
        int py = pos[y];

        assert (0 <= px && px < num);
        assert (0 <= py && py < num);

        assert (L[py] == -1 && R[py] == -1);

        int rx = R[px];
        if (rx != -1){
            L[rx] = py;

        }
        L[py] = px;
        R[py] = rx;
        R[px] = py;

    };

    auto del = [&](int x){
        int px = pos[x];
        assert (0 <= px && px < num);

        int lx = L[px];
        int rx = R[px];

        assert (lx + rx > -2); 
        if (lx == -1){
            assert (rx != -1);
            L[rx] = -1;
            top = rx;
        }
        else if (rx == -1){
            assert (lx != -1);
            R[lx] = -1;
        }
        else {
            assert (lx != -1);
            assert (rx != -1);
            L[rx] = lx;
            R[lx] = rx;
        }
        
        L[px] = -1;
        R[px] = -1;
    };

    for (auto [t,x,y] : Q){
        if (t == 1){
            add(x,y);
        }

        if (t == 2){
            del(x);
        }
    }

    int now = top;
 
    cout << rpos[now];
    while (R[now] != -1){
        now = R[now];
        cout << " " << rpos[now];
    }

    cout << endl;
    return 0;

}
