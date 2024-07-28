#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <complex>
#include <deque>
#include <forward_list>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <optional>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n),B(n);
    for (int i = 0; i < n; i++){
        cin >> A[i] >> B[i];
    }

    vector<long long> dp(1<<n);

    for (int bi = (1<<n)-1; bi >= 0; bi--){
        int num = 0;
        for (int i = 0; i < n; i++){
            if (bi >> i & 1) num++;
        }
        if (num%2) continue;

        int win = -1;
        for (int x = 0; x < n; x++){
            if (bi >> x & 1) continue;
            for (int y = 0; y < x; y++){
                if (bi >> y & 1) continue;

                if (A[x] == A[y] || B[x] == B[y]){
                    if (dp[bi|(1<<x)|(1<<y)] == -1) win = 1;
                }
            }
        }
        dp[bi] = win;
    }

    cout << (dp[0] == 1 ? "Takahashi" : "Aoki") << endl;

    
    return 0;

}