#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;
struct top2{
    long long score1,score2;
    int color1,color2;

    top2(long long s1 = -INF, int c1 = -1, long long s2 = -INF, int c2 = -1) : score1(s1), color1(c1), score2(s2), color2(c2) {}

    long long get(int color){
        if (color1 != color) return score1;
        return score2;
    }

    void add(long long score, int color){
        if (color1 == color){
            score1 = max(score,score1);
        } else if (color2 == color){
            score2 = max(score,score2);
            if (score1 < score2){
                swap(score1,score2);
                swap(color1,color2);
            }
        } else{
            if (score1 <= score){
                swap(score1,score2);
                swap(color1,color2);
                score1 = score;
                color1 = color;

            }
            else if (score2 < score){
                score2 = score;
                color2 = color;

            }
        }

    }

};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,k;
    cin >> n >> k;
    vector<int> C(n);
    vector<long long> V(n);
    for (int i = 0; i < n; i++){
        cin >> C[i] >> V[i];
    }

    const long long INF = 1e18;
    vector<top2> dp(k+1);
    dp[0] = top2(0,-1,-INF,-1);
       
    for (int i = 0; i < n; i++){
        vector<top2> ndp(k+1);
        for (int j = 0; j < k; j++){
            ndp[j+1] = dp[j];
        }
        for (int j = 0; j < k+1; j++){
            long long score = dp[j].get(C[i]);
            ndp[j].add(score+V[i],C[i]);
        }
        swap(dp,ndp);
    }

    long long ans = dp[k].score1;

    if (ans < 0) ans = -1;

    cout << ans << endl;
}
