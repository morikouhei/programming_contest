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
    vector<pair<int,int>> AB;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        AB.emplace_back(a,0);
    }
    for (int i = 0; i < m; i++){
        int b;
        cin >> b;
        AB.emplace_back(b,1);
    }
    sort(AB.begin(),AB.end());
    for (int i = 0; i < n+m-1;i++){
        if (AB[i].second == AB[i+1].second && AB[i].second == 0){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;

}