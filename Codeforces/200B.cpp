#include<bits/stdc++.h>
#include<cmath>
#include <iostream>
using namespace std;

int main(){

    int n,i,temp;
    double result=0.0;

    cin>>n;
    double val = n*1.00;

    for(i=0;i<n;i++){
        cin>>temp;
        //cout<<temp<<endl;
        result = result + temp;
    }
    //cout<<result<<endl;
    cout<<double(result/val)<<endl;
}
