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
    
    int n,k;
    cin >> n >> k;
    string S;
    cin >> S;

    // S をソート
    sort(S.begin(), S.end());

    auto f = [&](string T){

        for (int i = 0; i < n-k+1; i++){
            string U = T.substr(i, k);
            // U が回文かどうか判定
            if (U == string(U.rbegin(), U.rend())) return false;
        }
        return true;
    };

    long long ans = 0;
    // S の 文字列の並び替えを n! 通り全探索
    do {
        string T = S;
        if (f(T)) ans++;
    } while (next_permutation(S.begin(), S.end()));

    cout << ans << endl;

    return 0;

}