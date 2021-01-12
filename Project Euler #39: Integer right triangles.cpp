using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
inline ll Mod(ll x, ll mod) { return x % mod >= 0 ? x % mod : x % mod + mod; }

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    //clock_t s=clock();
    int *primiter = new int[5000 * 1000 + 1];
    memset(primiter, 0, sizeof(primiter));
    for (int m = 1; m <= 2000; m++)
    {
        for (int n = 1; n < m; n++)
        {
            if ((m + n) % 2 && __gcd(m, n) == 1)
            {
                int p = 2 * m * m + 2 * m * n;
                if (p > 5000000)
                    continue;
                primiter[p]++;
                int i = 2;
                while (i * p <= 5000000)
                {
                    primiter[i * p]++;
                    i++;
                }
            }
        }
    }
    int *ans = new int[5000 * 1000 + 1];
    //cout << (clock()-s)/CLOCKS_PER_SEC ;
    ans[12] = 12;
    for (int i = 13; i <= 5000 * 1000; i++)
    {
        if (primiter[i] > primiter[ans[i - 1]])
        {
            ans[i] = i;
        }
        else
            ans[i] = ans[i - 1];
    }
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        cout << ans[n] << '\n';
    }
    delete[] primiter;
    delete[] ans;
}
