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

    int n;
    cin >> n;
    vector<int> A(n),W(n);
    for (auto &a : A) cin >> a;
    for (auto &w : W) cin >> w;
    int sum = 0;

    vector<vector<int>> C(n);

    for (int i = 0; i < n; i++)
    {
        C[A[i]-1].push_back(W[i]);
    }

    for (int i = 0; i < n; i++)
    {
        if (C[i].size() == 0) continue;
        sort(C[i].begin(), C[i].end());

        for (int j = 0; j < C[i].size()-1; j++)
        {
            sum += C[i][j];
        }
    }

    cout << sum << endl;
}