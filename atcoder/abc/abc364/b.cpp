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

    int h,w;
    cin >> h >> w;
    int si,sj;
    cin >> si >> sj;
    si--,sj--;
    vector<string> C(h);
    for (auto &c: C) cin >> c;
    string X;
    cin >> X;

    for (char x: X){
        int dx = 0,dy = 0;
        if (x == 'L') dx = 0, dy = -1;
        if (x == 'R') dx = 0, dy = 1;
        if (x == 'U') dx = -1, dy = 0;
        if (x == 'D') dx = 1, dy = 0;
        int ni = si + dx, nj = sj + dy;
        if (ni < 0 || ni >= h || nj < 0 || nj >= w || C[ni][nj] == '#') continue;
        si = ni, sj = nj;
    }
    cout << si+1 << " " << sj+1 << endl;
    
    
    return 0;

}