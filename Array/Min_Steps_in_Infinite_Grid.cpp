#include<bits/stdc++.h>
#include <iostream>
using namespace std;

/*(x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
*/

//editorial
/*
class Solution {
public:
    int coverPoints(vector<int> x, vector<int> y) {
        if (x.size() <= 1) return 0;
        assert(x.size() == y.size());
        int ans = 0;
        for (int i = 1; i < x.size(); i++) {
            ans += max(abs(x[i] - x[i-1]), abs(y[i] - y[i-1]));
        }
        return ans;
    }
};
*/

//fastest
/*
int Solution::coverPoints(vector<int> &A, vector<int> &B) {
    int n,a,b,distance = 0;
    for( n = 1 ; n < A.size(); n++)
         {
             a = (A[n] > A[n-1]) ? A[n] - A[n-1] : A[n-1] - A[n];
             b = (B[n] > B[n-1]) ? B[n] - B[n-1] : B[n-1] - B[n];
             if(a>b)
                distance += a;
            else
               distance += b;

         }
    return distance;
}
*/

//lightweight
/*
int Solution::coverPoints(vector<int> &A, vector<int> &B) {

    int count=A.size();
    int i=0;
    int steps=0,diff=0;
    for(i=1;i<count;i++){
        if(abs(A[i]-A[i-1])==abs(B[i]-B[i-1]))
        {
            steps+=abs(A[i]-A[i-1]);
        }
        else if((diff=abs(abs(A[i]-A[i-1])-abs(B[i]-B[i-1])))>0)
        {
            if(abs(A[i]-A[i-1])>abs(B[i]-B[i-1]))
            {
                steps+=(diff+abs(B[i]-B[i-1]));
            }
            else
            {
                steps+=(diff+abs(A[i]-A[i-1]));
            }
        }
    }
    return steps;
}

*/

int main()
{
    int a[100],b[100];
    int sizeA;
    cin>>sizeA;

    for(int i=0; i<sizeA; i++)
    {
        cin>>a[i];
    }

    int sizeB;
    cin>>sizeB;

    for(int i=0; i<sizeB; i++)
    {
        cin>>b[i];
    }

    int dir=0;
    int x=a[0];
    int y=b[0];

    for(int i=0; i<sizeA; i++)
    {
        if(i==0) continue;
        else
        {
            if(x==a[i] || y==b[i])
                dir++;
            else
                dir=dir+2;
        }
        x=a[i];
        y=a[i];

    }
    cout<<dir<<endl;
    return 0;
}
