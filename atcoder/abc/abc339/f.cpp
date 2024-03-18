#include <bits/stdc++.h>
using namespace std;

bool is_prime(long long p)
{
    for (int i = 2; i * i <= p; i++)
    {
        if (p % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<string> A(n);
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    vector<long long> primes;

    int size = 10;
    long long M = 1e9;

    while (primes.size() < size)
    {
        long long p = rand() % M;
        if (is_prime(p))
        {
            primes.push_back(p);
        }
    }

    vector<vector<long long>> hash_list(n);

    for (int i = 0; i < n; i++)
    {
        for (auto p : primes)
        {
            long long x = 0;

            for (char c : A[i])
            {
                x = (x * 10 + c - '0') % p;
            }
            hash_list[i].push_back(x);
        }
    }

    map<vector<long long>, int> dic;
    for (int i = 0; i < n; i++)
    {
        dic[hash_list[i]]++;
    }

    auto mul = [&](int x, int y)
    {
        vector<long long> m;
        for (int i = 0; i < size; i++)
        {
            m.push_back(hash_list[x][i] * hash_list[y][i] % primes[i]);
        }
        return m;
    };

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            vector<long long> m = mul(i, j);
            ans += dic[m];
        }
    }

    cout << ans << endl;

    return 0;
}
