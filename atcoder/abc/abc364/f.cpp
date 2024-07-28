
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

    int n,q;
    cin >> n >> q;
    vector<tuple<int,int,int>> queries;
    for (int i = 0; i < q; i++) {
        int l,r,c;
        cin >> l >> r >> c;
        queries.emplace_back(l,r,c);
    }
    sort(queries.begin(),queries.end(),[](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });

    dsu uf(n);
    long long ans = 0;
    for (auto [l,r,c] : queries) {
        l--;
        r--;
        ans += c;
        if (uf.same(l,r)) {
            continue;
        }
        while (!uf.same(l,r)) {
            
            int l2 = l;
            int r2 = r;
            while (l2 + 1 < r2) {
                int m = (l2+r2)/2;
                if (uf.same(l,m)) {
                    l2 = m;
                } else {
                    r2 = m;
                }
            }
            uf.merge(l,r2);
            ans += c;
            l = r2;
        }
    }
    if (uf.size(0) != n) {
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }

}
