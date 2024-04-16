#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> count(100);
    string S;
    cin >> S;
    for (char c: S){
        count[c-'a']++;
    }
    vector<int> nums(101);
    for (auto c: count){
        nums[c]++;
    }
    for (int i = 1; i <= 100; i++){
        if (nums[i] != 0 && nums[i] != 2){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;

    return 0;
}
