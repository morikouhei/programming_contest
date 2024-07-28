
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


int main() {
    string S;
    cin >> S;

    vector<int> sa = suffix_array(S);

    auto lower = [&](string T) {
        int l = -1, r = S.size();
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (S.compare(sa[m], T.size(), T) < 0) {
                l = m;
            } else {
                r = m;
            }
        }
        return r;
    };
    auto upper = [&](string T) {
        int l = -1, r = S.size();
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (S.compare(sa[m], T.size(), T) <= 0) {
                l = m;
            } else {
                r = m;
            }
        }
        return r;
    };

    int q;
    cin >> q;
    for (int i = 0; i < q; ++i) {
        string T;
        cin >> T;
        cout << upper(T) - lower(T) << endl;
       
    }

}