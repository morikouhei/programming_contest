#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    long long n;
    cin >> n;
    
    string s = "02468";

    string ans = "";
    n --;

    if (n == 0){
        cout << 0 << endl;
        return 0;
    }
    while (n){
        int m = n%5;
        ans = s[m] + ans;
        n /= 5;
    }
    cout << ans << endl;
    return 0;

}
