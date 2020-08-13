#include<bits/stdc++.h>
#include<cmath>
#include <iostream>
using namespace std;

int main(){

    long long int n,k,result;
    cin>>n>>k;
    //cout<<ceil(n/2.0)<<endl;
    if (k <= ceil(n/2.0)){
        result = 2*(k-1)+1;
        cout<<result<<endl;
    }
    else{
        result = 2*(k-ceil(n/2.0));
        cout<<result<<endl;
    }

}
