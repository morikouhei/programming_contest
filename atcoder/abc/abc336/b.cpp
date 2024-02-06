#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n;
    cin >> n;
    
    for (int i = 0; i < 30; i++){
        if (n >> i & 1) {
            cout << i << endl;
            return 0;
        }
    }
    return 0;

}
