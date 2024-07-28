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

    vector<int> rect1(6), rect2(6);
    for (int i = 0; i < 6; i++) cin >> rect1[i];
    for (int i = 0; i < 6; i++) cin >> rect2[i];

    // rect1 ,2 に共通面積があるかどうか
    if (rect1[0] >= rect2[3] || rect1[3] <= rect2[0] || rect1[1] >= rect2[4] || rect1[4] <= rect2[1] || rect1[2] >= rect2[5] || rect1[5] <= rect2[2]){
        cout << "No" << endl;
    } else {
        cout << "Yes" << endl;
    }    

    
    
    return 0;

}