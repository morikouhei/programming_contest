#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    int n;
    cin >> n;

    vector<int> A(n);

    for (int i = 0; i < n; i++){
        cin >> A[i];
    }

    vector<int> c(n,0);

    int pos = -1;
    for (int i = 0; i < n; i++){
        int a = A[i];
        a--;
        if (a == -2) {
            pos = i;
        } else {
            c[a] = i;
        }

    }
    for (int i = 0; i < n; i++){
        cout << pos+1 << " ";
        pos = c[pos];
    }

    cout << endl;
    
    return 0;

}
