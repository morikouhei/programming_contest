#include <bits/stdc++.h>
using namespace std;

template <typename T>
T extgcd(T a, T b, T &x, T &y)
{
    T d = a;
    if (b != 0)
    {
        d = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
    }
    else
    {
        x = 1;
        y = 0;
    }
    return d;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    cin >> x >> y;

    long long x1, y1;
    extgcd(abs(x), abs(y), y1, x1);

    long long base = abs(abs(x) * y1 + abs(y) * x1);
    if (base > 2)
    {
        cout << -1 << endl;
        return 0;
    }

    x1 *= 2 / base;
    y1 *= 2 / base;

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            long long count = 0;

            long long x2 = x1, y2 = y1;
            // cout << x2 << " " << y2 << endl;
            if (i)
                x2 *= -1;
            if (j)
                y2 *= -1;

            count += x * y2 - y * x2;

            if (abs(count) == 2 && abs(x2) <= 1e18 && abs(y2) <= 1e18)
            {
                cout << x2 << " " << y2 << endl;
                return 0;
            }
        }
    }

    cout << -1 << endl;

    return 0;
}
