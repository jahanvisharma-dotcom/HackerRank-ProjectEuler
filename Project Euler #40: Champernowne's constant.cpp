#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define debug(x) cout << #x << " = " << x << endl
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
inline ll Mod(ll x, ll mod) { return x % mod >= 0 ? x % mod : x % mod + mod; }

vector<ll> s(17, 0);
ll tavan[19] = {1};

int give_digit(ll ans, int n)
{
    stringstream q, pp;
    q << ans;
    string answer;
    q >> answer;
    pp << answer[n - 1];
    int nn;
    pp >> nn;
    //cout << nn << '\n' ;
    return nn;
}

int solve(ll n)
{
    int j = lower_bound(all(s), n) - s.begin();
    int i = j - 1;
    n -= s[i];
    ll ans = tavan[i];
    ans += (n / j);
    n = n % j;
    if (!n)
    {
        ans -= 1;
        //cout << ans%10 << '\n' ;
        return ans % 10;
    }
    return give_digit(ans, n);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    ll p = 9;
    s[1] = p;
    tavan[1] = 10;
    for (int i = 2; i < 17; i++)
    {
        tavan[i] = tavan[i - 1] * 10;
        p *= 10;
        s[i] = s[i - 1] + p * i;
    }
    tavan[17] = tavan[16] * 10;
    tavan[18] = tavan[17] * 10;
    int t;
    cin >> t;
    while (t--)
    {
        int ans = 1;
        for (int i = 0; i < 7; i++)
        {
            ll p;
            cin >> p;
            ans *= solve(p);
        }
        cout << ans << '\n';
    }
}
