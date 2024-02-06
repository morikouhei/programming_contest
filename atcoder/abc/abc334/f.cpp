
#include<bits/stdc++.h>
#include <atcoder/segtree>
using namespace atcoder;
using namespace std;

const double INF = 1e18;
double op(double a, double b){ return min(a,b);}
double e() {return INF;}

double dist (vector<int> S, vector<int> T){
        int x = S[0];
        int y = S[1];
        int nx = T[0];
        int ny = T[1];
        return hypot(x-nx,y-ny);
    }
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int N,K;
    cin >> N >> K;

    vector<int> S(2);
    cin >> S[0] >> S[1];

    vector<vector<int>> XY(N,vector<int>(2));
    for (int i = 0; i < N ; i++){
        cin >> XY[i][0] >> XY[i][1];
    }

    XY.push_back(S);
    

    segtree<double, op, e> seg(N+1);

    seg.set(0,0);

    for (int i = 1; i <= N; i++){
        double d = dist(XY[i-1],S) + dist(XY[i],S) - dist(XY[i],XY[i-1]);

        double best = seg.prod(max(0,i-K),i);
        seg.set(i,best+d);
    }

    double ans = seg.get(N);

    ans += dist(XY[0],S);
    for (int i = 1;i <= N;i ++){
        ans += dist(XY[i],XY[i-1]);
    };

    cout << fixed << setprecision(15) << ans << endl;

    return 0;

}
