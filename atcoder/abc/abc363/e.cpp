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
    
    int h,w,y;
    cin >> h >> w >> y;
    vector<vector<int>> A(h, vector<int>(w));
    for (auto &a : A) for (auto &b : a) cin >> b;
    int ans = h * w;

    // 最小値を取り出すための priority_queue
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> p;
    for (int i = 0; i < h; i++){
        p.emplace(A[i][0], make_pair(i, 0));
        p.emplace(A[i][w-1], make_pair(i, w-1));
    }
    for (int i = 1; i < w-1; i++){
        p.emplace(A[0][i], make_pair(0, i));
        p.emplace(A[h-1][i], make_pair(h-1, i));
    }
    vector<vector<bool>> visited(h, vector<bool>(w, false));
    for (int i = 1; i <= y; i++){
        while (!p.empty()){
            auto [value, pos] = p.top();
            if (value > i) break;

            p.pop();
            auto [x, y] = pos;
            if (visited[x][y]) continue;
            visited[x][y] = true;
            ans -= 1;
            if (x > 0) p.emplace(A[x-1][y], make_pair(x-1, y));
            if (x < h-1) p.emplace(A[x+1][y], make_pair(x+1, y));
            if (y > 0) p.emplace(A[x][y-1], make_pair(x, y-1));
            if (y < w-1) p.emplace(A[x][y+1], make_pair(x, y+1));
        }
        cout << ans << endl;
    }

    return 0;

}