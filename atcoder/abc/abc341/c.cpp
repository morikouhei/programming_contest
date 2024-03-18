#include <bits/stdc++.h>
using namespace std;


int solve(int x, int y, vector<string>& S, string& T){

    for (char t: T){
        if (t == 'L') y--;
        if (t == 'R') y++;
        if (t == 'U') x--;
        if (t == 'D') x++;

        if (S[x][y] == '#'){
            return 0;
        }
    }
    return 1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h,w,n;
    cin >> h >> w >> n;
    
    string T;
    cin >> T;
    vector<string> S(h);
    for (auto& s: S) cin >> s;
    int ans = 0;
    for (int x = 0; x < h; x++){
        for (int y = 0; y < w; y++){
            if (S[x][y] == '#') continue;
            ans += solve(x,y,S,T);
        }
    }

    cout << ans << endl;
    return 0;
}
