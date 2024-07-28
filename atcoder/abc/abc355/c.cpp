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

    int n,t;
    cin >> n >> t;

    vector<int> countX(n),countY(n);
    int cross = 0,rcross = 0;
    for (int i = 0; i < t; i++){
        int a;
        cin >> a;
        a -= 1;
        int x = a/n;
        int y = a%n;

        countX[x]++;
        countY[y]++;
        if (countX[x] == n || countY[y] == n){
            cout << i+1 << endl;
            return 0;
        }
        if (x == y) cross++;
        if (n-1-x == y) rcross++;

        if (cross == n || rcross == n){
            cout << i+1 << endl;
            return 0;
        }

    }
    cout << -1 << endl;

    return 0;

}