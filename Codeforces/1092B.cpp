#include<bits/stdc++.h>

using namespace std;


int main(){

    int n,temp,result=0;
    cin>>n;
    int arr[n];

    for(int i=0;i<n;i++){
        cin>>temp;
        arr[i] = temp;
    }
    //sort(arr, arr+n, greater<int>());
    sort(arr, arr+n);
    /*
    for(int i=0;i<n;i++){
        cout<<arr[i]<<endl;
    }
    */
    for(int i=0;i<n;i=i+2){
        result += abs(arr[i]-arr[i+1]);
    }
    cout<<result<<endl;

}
