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

    long long sx,sy,tx,ty;
    cin >> sx >> sy >> tx >> ty;
    if ((sx+sy)%2) {
        sx--;
    }
    if ((tx+ty)%2) {
        tx--;
    }

    long long dx = abs(tx-sx);
    long long dy = abs(ty-sy);
    cout << (dy + max(dx,dy))/2 << endl;
    
    return 0;

}