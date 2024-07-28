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
    
    long long n;
    cin >> n;

    // 1-9 と "*" を使った 回文の式で n になるものを作る
    vector<long long> factors;
    for (long long i = 1; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            factors.push_back(i);
            if (i * i != n)
            {
                factors.push_back(n / i);
            }
        }
    }
    // factors から 
    // 0 を含むもの, 回文ではなく reverse した数が factors に含まれないものを除外
    vector<long long> cand;
    for (long long f : factors)
    {
        string s = to_string(f);
        bool ok = true;
        for (char c : s)
        {
            if (c == '0')
            {
                ok = false;
            }
        }
        if (ok)
        {
            string t = s;
            reverse(t.begin(), t.end());
            ok = false;
            if (find(factors.begin(), factors.end(), stoll(t)) != factors.end())
            {
                ok = true;
            }
        }
        if (ok)
        {
            cand.push_back(f);
        }
    }

    // dp によって回文の式を求める
    // pair<string,string> はそれぞれの式の左辺と中央に置く文字列
    // 2 * 3 * 2 の時は {"2,","3"} のように持つ

    map<pair<long long,int>, pair<string,string>> dp;
    dp[{1,0}] = {"",""};
    for (auto f: cand){
        bool is_palindrome = false;
        string s = to_string(f);
        string t = s;
        reverse(t.begin(), t.end());
        long long rf = stoll(t);
        if (s == t){
            is_palindrome = true;
        }

        map<pair<long long,int>, pair<string,string>> next;

        for (auto [value, expr]: dp){
            // f を使わない場合
            next[value] = expr;

            // f を使う場合
            // 使う回数を探索する
            auto [nvalue, mid] = value;

            pair<string,string> next_expr = expr;
            while (n%nvalue == 0){
                // 真ん中に f を使う場合
                if (is_palindrome && next_expr.second == ""){
                    if (n / nvalue >= f && n%(nvalue * f) == 0){
                        next[{nvalue * f,1}] = {next_expr.first, s};
                    }
                }

                // 左側に f を使う場合
                // オーバーフローしないように 判定
                if (n/nvalue < f) break;
                nvalue *= f;
                if (nvalue > n) break;
                if (n/nvalue < rf) break;
                nvalue *= rf;
                if (nvalue > n) break;

                if (n%(nvalue) == 0) {
                    int nmid = next_expr.second == "" ? 0 : 1;
                    next[{nvalue,nmid}] = {next_expr.first + s + ",", next_expr.second};
                }
                if (f == 1) break;
                next_expr.first += s + ",";
            }
        }
        dp = next;
    }
    if (dp.find({n,0}) == dp.end() && dp.find({n,1}) == dp.end()){
        cout << -1 << endl;
    } else {
        string left,mid;
        if (dp.find({n,0}) != dp.end()){
            auto [l,m] = dp[{n,0}];
            left = l;
            mid = m;
        } else {
            auto [l,m] = dp[{n,1}];
            left = l;
            mid = m;
        }
        // left は "," を "*" に置換
        for (char &c: left){
            if (c == ',') c = '*';
        }
        string right = left;
        reverse(right.begin(), right.end());
        string ans = "";
        if (mid == ""){
            left.pop_back();
            ans = left + right;
        } else {
            ans = left + mid + right;
        }
        cout << ans << endl;
    }

    return 0;

}