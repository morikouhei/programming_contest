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
    vector<string> S(n);
    vector<long long> C(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> S[i] >> C[i];
    }

    auto is_palindrome = [&](string s, string t) -> bool {
        for (int i = 0; i < min(s.size(), t.size()); ++i)
        {
            if (s[i] != t[i])
            {
                return false;
            }
        }
        return true;

    };

    map<pair<string,int>, long long> dp;
    priority_queue<pair<long long, pair<string,int>>, vector<pair<long long, pair<string,int>>>, greater<pair<long long, pair<string,int>>>> h;

    auto add = [&](string s, int dir, long long c) {
        if (dp.find({s,dir}) == dp.end() || dp[{s,dir}] > c)
        {
            dp[{s,dir}] = c;
            h.push({c, {s,dir}});
        }
    };

    auto try_add = [&](string first, string second, long long c) {

        if (!is_palindrome(first,second)) return ;

        if (first.size() > second.size())
        {
            string s = first.substr(second.size());
            add(s, 1, c);
        } else if (first.size() < second.size())
        {
            string s = second.substr(first.size());
            add(s, -1, c);
        } else
        {
            add("", 0, c);
        }
        
    };

    for (int i = 0; i < n; i++){

        for (int j = 0; j < S[i].length(); j++)
        {
            string s = S[i].substr(0,j);
            string t = S[i].substr(j);
            reverse(s.begin(), s.end());
            try_add(s,t,C[i]);

            s = S[i].substr(0,j);
            t = S[i].substr(j+1);
            reverse(s.begin(), s.end());
            try_add(s,t,C[i]);
        }
    }
    while (!h.empty()){
        auto [c, p] = h.top();
        h.pop();
        if (dp[p] < c) continue;

        string s = p.first;
        int dir = p.second;

        if (s == "")
        {
            cout << c << endl;
            return 0;
        }
        if (dir == -1)
        {
            for (int i = 0; i < n; i++)
            {
                string t = S[i];
                reverse(t.begin(), t.end());
                try_add(t,s,c+C[i]);
            }
        } else if (dir == 1)
        {
            for (int i = 0; i < n; i++)
            {
                string t = S[i];
                try_add(s,t,c+C[i]);
            }
        }
    }
    cout << -1 << endl;

    return 0;

}