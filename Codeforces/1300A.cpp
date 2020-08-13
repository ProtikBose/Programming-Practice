#include<bits/stdc++.h>
#include<cmath>
#include <iostream>
using namespace std;

int main(){

    int t;
    cin>>t;

    while(t){
        int n,sum=0,temp,result=0;
        cin>>n;

        for(int i=0;i<n;i++){
            cin>>temp;
            if(temp==0) result++;
            sum = sum+temp;

        }
        if(sum+result!=0) cout<<result<<endl;
        else{
            cout<<result+1<<endl;
        }
        t--;
    }

}
