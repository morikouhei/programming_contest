#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for (auto& a: A) cin >> a;

    int M = 2e5+5;
    vector<int> divisor(M,-1);

    for (int i = 1; i < M; i++) divisor[i] = i;
    for (int i = 2; i * i < M; i++) {
        if (divisor[i] == i) {
            for (int j = i * i; j < M; j += i) {
                if (divisor[j] == j) divisor[j] = i;
            }
        }
    }

    long long ans = 0;
    map<int,long long> count;
    int zero = 0;
    for (int i = 0; i < n; i++){
        int a = A[i];

        if (a == 0){
            ans += n-1-zero;
            zero++;
            continue;
        }
        int num = 1;

        while (a != 1){
            int x = divisor[a];
            int count = 0;
            while (a % x == 0){
                a /= x;
                count++;
            }
            if (count%2) num *= x;
        }

        ans += count[num];
        count[num]++;

    }

    cout << ans << endl;


    return 0;
}
