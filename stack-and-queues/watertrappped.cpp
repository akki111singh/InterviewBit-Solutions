#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef long double ld;
 
#define lp(var,start,end) for (ll var = start; var <end ; ++var)
#define rlp(var,start,end) for(ll var = start; var>=end ; var--)
#define pb push_back
#define mp make_pair
#define pf push_front
#define ff first
#define ss second
#define vll vector<ll>
#define vld vector<ld>
#define pll pair<ll,ll> 
#define pld pair<ld,ld> 
#define vpll vector<pll>
#define vpld vector<pld>
#define all(X) X.begin(),X.end()
#define endl "\n"
#define sz(x) ((ll)((x).size()))
 
const ll N=1e5+5,inf=1e18;

ll power(ll x, ll y, ll p) 
{ 
    ll res = 1;  
    x = x % p;  
    while (y > 0) { 
        if (y%2) res = (res * x) % p; 
        y = y/2; 
        x = (x * x) % p; 
    } 
    return res; 
} 

int trap(const vector<int> &A) {
    int n = A.size();
    vector<int> a(n + 1, 0);
    for(int i=1;i<=n;i++) a[i] = A[i-1];
    stack <int> s;
    vector <int> l(n + 1), r(n + 1);
    s.push(1);
    for(int i = 2; i <= n; i++){
    	while(!s.empty() && a[s.top()] < a[i]) s.pop();
    	if(s.empty()) l[i] = 0;
    	else l[i] = s.top();
        if(s.empty()) s.push(i);
    	else if(a[i] >= a[s.top()]) s.push(i);
    }
    while(!s.empty()) s.pop();
    s.push(n);
    r[n] = n;
    for(int i = n-1; i >= 1; i--){
    	while(!s.empty() && a[s.top()] < a[i]) s.pop();
    	if(s.empty()) r[i] = n;
    	else r[i] = s.top();
        if(s.empty()) s.push(i);
    	else if(a[i] >= a[s.top()]) s.push(i);
    }
    int ans = 0;
    for(int i=1;i<=n;i++){
        if( min(a[l[i]],a[r[i]]) > a[i]){
            ans += (min(a[l[i]],a[r[i]]) - a[i]);
            // cout << "i is "<< i << " ans is "<< (min(a[l[i]],a[r[i]])-a[i]) << endl;
        }
    }

    cout << ans << endl;
}

int main(){
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    // int n;
    // cin >> n;
    vector<int> A = {6};
    // for(int i=0;i<n;i++) cin >> A[i];
    trap(A);
    return 0;
}