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

vector<string> dfs(int n){
    if (n == 0){
        vector<string> ans(1,"#");
        return ans;
    }

    auto nans = dfs(n-1);
    int size = nans.size() * 3;

    vector<string> ans(size,string(size,'.'));

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (i == 1 && j == 1) continue;
            for (int x = 0; x < nans.size(); x++){
                for (int y = 0; y < nans.size(); y++){
                    ans[i*nans.size()+x][j*nans.size()+y] = nans[x][y]; 
                }
            }
        }
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    auto ans = dfs(n);

    for (auto s: ans){
        cout << s << endl;
    }


    return 0;
}
