#include <bits/stdc++.h>
using namespace std;


int search(const vector<int> &A, int B) {
    int ans = -1;
    for(int i=0;i<A.size();i++){
      if(A[i] == B){
          ans = i;
          break;
      }
    }
    return ans;
}


int main()
{
    cout << search(5) << endl;
    return 0;
}