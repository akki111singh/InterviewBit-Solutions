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

void show_quiz(unordered_multiset <int, greater <int> > gquiz1){
    unordered_multiset <int, greater <int> > :: iterator itr;
    for (itr = gquiz1.begin(); itr != gquiz1.end(); ++itr) 
    { 
        cout << *itr<<" "; 
    } 
    cout << endl; 
}

vector<int> slidingMaximum(const vector<int> &A, int B) {
    int n = A.size();
    unordered_multiset <int, greater <int> > q;
    vector<int> ans;
    unordered_multiset <int, greater <int> > :: iterator itr;
    for(int i=0;i<B;i++) q.insert(A[i]);
    itr = q.begin();
    show_quiz(q);
    ans.push_back(*itr);
    for(int i=0;i<n-B;i++){
        q.erase(A[i]);
        q.insert(A[i+B]);
        show_quiz(q);
        itr = q.begin();
        ans.push_back(*itr);
    }
    return ans;
}

int main(){
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    
    int B;
    vector<int> A = {90, 767, 90, 777, 463, 196, 984, 277, 451, 643, 403, 316, 451, 967, 683, 786, 167, 372, 758, 402, 325, 431, 351, 351, 158, 663, 244, 559, 345, 759, 924, 585, 509, 397, 540, 869, 997, 670, 375, 180, 48, 936, 203, 8, 598, 703, 733, 333, 414, 377, 496, 351, 910, 685, 612, 773, 571, 24, 679, 174, 644, 639, 544, 1, 884, 982, 447, 670, 251, 868, 815, 467, 386, 932, 178, 295, 957, 757, 124, 932, 342, 301, 406, 259, 943, 79, 313, 218};
    // for(int i=0;i<n;i++) cin >> A[i];
    // cin>> B;
    B = 7;
    vector<int> ans = slidingMaximum(A,B);
    for(int i=0;i<ans.size();i++) cout << ans[i]<< " ";
    cout << endl;
    return 0;
}

// 984 984 984 984 984 984 984 967 967 967 967 967 967 967 786 786 758 758 758 663 663 663 663 759 924 924 924 924 924 924 997 997 997 997 997 997 997 936 936 936 936 936 733 733 733 733 910 910 910 910 910 910 910 773 773 773 679 679 884 982 982 982 982 982 982 982 868 932 932 932 957 957 957 957 957 957 957 757 943 943 943 943


// 984 984 984 984 984 984 984 967 967 967 967 967 967 967 786 786 758 758 758 663 663 663 663 759 924 924 924 924 924 924 997 997 997 997 997 997 997 936 936 936 936 936 733 733 733 733 910 910 910 910 910 910 910 773 773 773 679 679 884 982 982 982 982 982 982 982 868 932 932 932 957 957 957 957 957 957 957 932 943 943 943 943 