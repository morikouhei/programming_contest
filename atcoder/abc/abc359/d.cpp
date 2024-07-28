
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
    int n,k;
    cin >> n >> k;
    string s;
    cin >> s;

    map<string, mint> dp;
    dp[string(k, '0')] = 1;

    auto is_palindrome = [&](string s) {
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != s[s.size()-1-i]) return false;
        }
        return true;
    };

    for (auto c : s) {
        map<string, mint> ndp;
        for (auto [key, val] : dp) {
            if (c != 'A'){
                string nkey = key.substr(1) + 'B';
                if (!is_palindrome(nkey)) {
                    ndp[nkey] += val;
                }
            }
            if (c != 'B'){
                string nkey = key.substr(1) + 'A';
                if (!is_palindrome(nkey)) {
                    ndp[nkey] += val;
                }
            }
            
        }
        dp = ndp;
    }
    mint ans = 0;
    for (auto [key, val] : dp) {
        ans += val;
    }
    cout << ans.val() << endl;

}