#include<bits/stdc++.h>
using namespace std;

const int INF = 100100100;

int solve(string &s, int k) {
    int n = s.size();

    int ans = INF;

    int x = 0, p = 0;
    for (int i = 0; i < n; i++){
        if (s[i] == '.') p++;
        if (s[i] == 'x') x++;

        if (i < k-1) continue;

        if (x == 0) {
            ans = min(ans,p);
        }

        if (s[i-k+1] == '.') p--;
        if (s[i-k+1] == 'x') x--;

    }

    return ans;

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int h,w,k;

    cin >> h >> w >> k;

    vector<string> S(h);
    for (auto &s: S) cin >> s;

    int ans = INF;

    for (int i = 0; i < 2; i++){
        for (auto &s: S) ans = min(ans,solve(s,k));

        vector<string> T(w,string(h,'.'));

        for (int x = 0; x < h; x++){
            for (int y = 0; y < w; y++){
                T[y][x] = S[x][y];
            }
        }

        swap(S,T);
        swap(h,w);

    }

    if (ans == INF) ans = -1;

    cout << ans << endl;


    return 0;

}
