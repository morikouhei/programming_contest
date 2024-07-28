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

    int xa,ya,xb,yb,xc,yc;
    cin >> xa >> ya >> xb >> yb >> xc >> yc;

    // 直角三角形かどうかを判定する

    // 三平方の定理を使う
    // 三平方の定理は、直角三角形の直角を挟む2辺の長さの2乗の和が、斜辺の長さの2乗に等しいというもの
    // 3辺の長さを求める
    vector<int> edges;
    edges.push_back((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb));
    edges.push_back((xb-xc)*(xb-xc) + (yb-yc)*(yb-yc));
    edges.push_back((xc-xa)*(xc-xa) + (yc-ya)*(yc-ya));
    sort(edges.begin(), edges.end());
    if (edges[0] + edges[1] == edges[2]){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }

    
    
    return 0;

}