#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    string S;
    cin >> S;
    for (int i = 0; i < S.size()-1;i++){
        if (S[i] > S[i+1]){
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
    
    return 0;

}
