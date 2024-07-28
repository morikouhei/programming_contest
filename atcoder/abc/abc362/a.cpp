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

    int r,g,b;
    cin >> r >> g >> b;
    string c;
    cin >> c;
    int mi = 100000;
    // red green blue の どれかを買う s == c のときは何もしない
    if (c != "Red"){
        mi = min(mi, r);
    }
    if (c != "Green"){
        mi = min(mi, g);
    }
    if (c != "Blue"){
        mi = min(mi, b);
    }
    cout << mi << endl;
    
    
    return 0;

}