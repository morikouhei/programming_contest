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

    int n,m;
    cin >> n >> m;
    vector<int> A(m);
    for (auto &a: A) cin >> a;

    vector<int> count(m);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            int x;
            cin >> x;
            count[j] += x; 
        }
    }
    bool ok = true;
    for (int i = 0; i < m; i++){
        if (A[i] > count[i]) ok = false;
    }

    cout << (ok ? "Yes":"No") << endl;

    return 0;
}
