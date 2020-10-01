#include <bits/stdc++.h>
using namespace std;

int sqrt(int A)
{
    if (A == 0 || A == 1)
        return A;
    int start = 1;
    int end = A;
    int ans;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (mid * mid == A)
            return mid;
        else if (mid * mid < A)
        {
            start = mid + 1;
            ans = mid;
        }

        else if (mid * mid > A)
            end = mid - 1;
    }
    return ans;
}

int main()
{
    cout << sqrt(5) << endl;
    return 0;
}