#include <bits/stdc++.h>
using namespace std;

struct Point{
    int x,y,z;
};


int calc_area(Point a, Point b, Point c){

    Point l,r;
    l.x = min({a.x,b.x,c.x});
    l.y = min({a.y,b.y,c.y});
    l.z = min({a.z,b.z,c.z});
    r.x = max({a.x,b.x,c.x});
    r.y = max({a.y,b.y,c.y});
    r.z = max({a.z,b.z,c.z});

    int ans = 1;
    ans *= max(0,l.x+7-r.x);
    ans *= max(0,l.y+7-r.y);
    ans *= max(0,l.z+7-r.z);

    return ans;

}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int v1,v2,v3;
    cin >> v1 >> v2 >> v3;

    if (v1 + v2 * 2 + v3 * 3 != 3 * 7 * 7 * 7){
        cout << "No" << endl;
        return 0;
    }

    vector<Point> Points;
    for (int x = -7; x <= 7; x++){
        for (int y = -7; y <= 7; y++){
            for (int z = -7; z <= 7; z++){
                Points.push_back({x,y,z});
            }
        }
    }
    Point a{0,0,0};

    for (Point b: Points){
        for (Point c: Points){

            if (calc_area(a,b,c) != v3) continue;

            if (calc_area(a,b,b) + calc_area(a,c,c) + calc_area(b,c,c) - v3 * 3 != v2) continue;

            cout << "Yes" << endl;

            cout << a.x << " " << a.y << " " << a.z << " " << b.x << " " << b.y << " " << b.z << " " << c.x << " " << c.y << " " << c.z << endl;
            return 0;

        }
    }


    return 0;
}
