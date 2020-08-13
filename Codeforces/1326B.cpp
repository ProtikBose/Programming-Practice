#include<bits/stdc++.h>

using namespace std;


int main(){

    int n;
    cin>>n;
    long long int result[n],temp,maxVal;

    for(int i=0;i<n;i++){
        cin>>temp;
        if(i==0){
            result[i] = temp;
            maxVal = temp;
        }
        else if(i==1){
            result[i] = temp+maxVal;
            maxVal = result[i]>maxVal?result[i]:maxVal;
        }
        else{
            maxVal = result[i-1]>maxVal?result[i-1]:maxVal;
            result[i] = temp+maxVal;
        }
    }

    for(int i=0;i<n;i++){
        if(i<n-1)
            cout<<result[i]<<" ";
        else cout<<result[i]<<endl;
    }
}
