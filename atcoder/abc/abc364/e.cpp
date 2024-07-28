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

    int n,x,y;
    cin >> n >> x >> y;
    vector<int> A(n),B(n);
    for (int i = 0; i < n; i++){
        cin >> A[i] >> B[i];
    }
    const int INF = 1e9;
    vector<vector<int>> dp(n+1,vector<int>(x+1,INF));
    dp[0][0] = 0;
    for (int i = 0; i < n; i++){
        for (int j = i; j >= 0; j--){
            for (int k = 0; k < x; k++){
                if (dp[j][k] > y) continue;
                if (k+A[i] > x) continue;
                dp[j+1][k+A[i]] = min(dp[j+1][k+A[i]],dp[j][k]+B[i]);
            }
        }
    }
    int ans = 0;
    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= x; j++){
            if (dp[i][j] != INF) ans = max(ans,i);
            if (i != n && dp[i][j] <= y) ans = max(ans,i+1);
        }
    }
    cout << ans << endl;
    
    return 0;

}