
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

using mint = modint1000000007;


// 座標構造体 P
struct P {
    int x;
    int y;

    // デフォルトコンストラクタ
    P() : x(0), y(0) {}

    // 座標を指定するコンストラクタ
    P(int xCoord, int yCoord) : x(xCoord), y(yCoord) {}

    // + 演算子のオーバーロード
    P operator+(const P& other) const {
        return P(x + other.x, y + other.y);
    }

    // - 演算子のオーバーロード
    P operator-(const P& other) const {
        return P(x - other.x, y - other.y);
    }

    // 内積を計算する関数
    int dot(const P& other) const {
        return x * other.x + y * other.y;
    }

    int cross(const P& other) const {
        return x * other.y - y * other.x;
    }

    // 2点を使って三角形の面積を計算する関数 (外積の半分)
    int area(const P& a, const P& b) const {
        return (a - *this).cross(b - *this);
    }

    // 偏角ソート用に角度を返す関数
    double angle() const {
        return std::atan2(y, x);
    }

    // 座標の表示
    void display() const {
        std::cout << "x: " << x << ", y: " << y << std::endl;
    }
};


int main() {

    int n;
    cin >> n;
    vector<P> p(n);
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        p[i] = P(x, y);
    }

    vector<pair<P,pair<int,int>>> edges;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; j++){
            if (i == j) continue;
            edges.push_back({p[i] - p[j], {i, j}});
        }
    }
    // 偏角ソート
    sort(edges.begin(), edges.end(), [&](auto a, auto b) {
        return a.first.angle() < b.first.angle();
    });

    vector<vector<vector<mint>>> dp(n, vector<vector<mint>>(n, vector<mint>(2, 0)));
    for (int i = 0; i < n; ++i) {
        dp[i][i][0] = 1;
    }

    vector<vector<vector<int>>> P_inside(n, vector<vector<int>>(n,vector<int>(n,0)));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            for (int k = 0; k < n; k++){
                if (i == j || j == k || k == i) continue;
                for (int l = 0; l < n; l++){
                    if (l == i || l == j || l == k) continue;
                    // l が三角形ijkの内部にあるかどうか
                    if (p[l].area(p[i], p[j]) >= 0 && p[l].area(p[j], p[k]) >= 0 && p[l].area(p[k], p[i]) >= 0){
                        P_inside[i][j][k]++;
                    }
                }
            }
        }
    }
    vector<mint> pow2(n+1, 1);
    for (int i = 1; i <= n; i++){
        pow2[i] = pow2[i-1] * 2;
    }

    for (int i = 0; i < edges.size(); ++i) {
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        for (int j = 0; j < n; ++j) {
            // j,a,b の 三角形の面積 mod2
            int s = abs(p[j].area(p[a], p[b])) % 2;
            for (int k = 0; k < 2; k++){
                dp[j][a][k^s] += dp[j][b][k] * pow2[P_inside[j][b][a]];
            }
        }
    }
    mint ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += dp[i][i][0]-1;
    }
    ans -= edges.size()/2;
    cout << ans.val() << endl;

}
