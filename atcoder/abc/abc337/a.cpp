#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n;
    cin >> n;
    int X=0,Y=0;

    for (int i = 0; i < n; i++){
        int x,y;
        cin >> x >> y;
        X += x;
        Y += y;
    }
    if (X > Y){
        cout << "Takahashi";
    }
    else if(X==Y) {
        cout << "Draw";
    }
    else {
        cout << "Aoki";
    }
    cout << endl;
    
    return 0;

}
