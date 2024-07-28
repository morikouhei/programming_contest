
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")

#include <atcoder/all>
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
using namespace atcoder;

using mint = modint998244353;

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for (auto& a : A) cin >> a;

    // 長さが i で 最後に選んだのが j で その１つ前が k のときの通り数
    vector<vector<vector<mint>>> dp(n + 1, vector<vector<mint>>(n, vector<mint>(n, 0)));

    for (int i = 0; i < n; ++i) {
        dp[1][i][i] += 1;
        for (int ni = 1; ni < n; ++ni) {
            for (int j = 0; j < i; ++j) {
                for (int k = 0; k <= j; ++k) {
                    if (dp[ni][j][k].val() == 0) continue;

                    if (ni == 1) {
                        dp[ni + 1][i][j] += dp[ni][j][k];
                    } else {
                        if (A[i]-A[j] == A[j]-A[k]) {
                            dp[ni + 1][i][j] += dp[ni][j][k];
                        }
                    }
                }
            }
        }
    }
    for (int i = 1; i <= n; i++){
        mint ans = 0;
        for (int j = 0; j < n; j++){
            for (int k = 0; k < n; k++){
                ans += dp[i][j][k];
            }
        }
        cout << ans.val() << endl;
    }

}