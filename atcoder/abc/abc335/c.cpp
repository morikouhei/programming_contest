
#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n,q;
    cin >> n >> q;

    vector<pair<int,int>> history;

    for (int i = n;i > 0;i--){
        history.emplace_back(i,0);
    }
    int x = 1;
    int y=0;



    for (int i=0;i<q;i++){
        int t;
        cin >> t;
        
        if (t == 1){
            char c;
            cin >> c;

            if (c == 'R'){
                x += 1;
            } else if (c == 'L'){
                x -= 1;
            } else if (c == 'U'){
                y += 1;
            } else {
                y -= 1;
            }
            history.emplace_back(x,y);
        } 
        else{
            int p;
            cin >> p;
            
            auto [x,y] = history[history.size()-p];
            cout << x << " " << y << endl;
        }
    }
    return 0;

}
