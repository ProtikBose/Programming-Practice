#include<bits/stdc++.h>

using namespace std;

int main(){

    int k,n,w;

    cin>>k>>n>>w;

    int total=k*(w*(w+1))/2;
    int result;
    if(total<=n) result=0;
    else
        result=total-n;
    cout<<result<<endl;


    return 0;

}
