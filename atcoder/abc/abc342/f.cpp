#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,l,d;
    cin >> n >> l >> d;
    int ma = max(l+d,n+d);
    vector<double> Y(ma,0);
    vector<double> Y_prob(ma,0);

    Y[0] = 1;
    double cum = 1;
    for (int i = 1; i < ma; i++){
        Y[i] = cum / d;
        cum += Y[i];
        if (i >= d) cum -= Y[i-d];

        if (i >= l){
            Y_prob[i] = Y[i];
            cum -= Y[i];
            Y[i] = 0;
        }
        Y_prob[i] += Y_prob[i-1];
    }

    double win_base = 1 - Y_prob[n];
    double win = 0;

    vector<double> X(ma,0);
    
    for (int i = ma-1; i >= 0; i--){
        if (i > n) continue;

        double win_stay = win_base;
        if (i) win_stay += Y_prob[i-1];
        double win_dice = win / d;

        X[i] = max(win_stay,win_dice);
        win += X[i];
        if (i+d < ma){
            win -= X[i+d];
        }
    }

    cout << fixed << setprecision(10) << X[0] << endl;



    return 0;
}
