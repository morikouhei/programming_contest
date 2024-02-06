
#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n;
    cin >> n;

    for (int x=0;x<=n;x++){
        for (int y=0;y<=n-x;y++){
            for (int z=0;z<=n-x-y;z++){
                if (x+y+z <= n){
                    cout << x << " " << y << " " << z << endl;
                }
            }
        }
    }
    return 0;

}
