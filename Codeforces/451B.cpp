#include<bits/stdc++.h>

using namespace std;


int main(){

    int n,res=0,posPrev=-1,posPost=-1;
    cin>>n;
    long long int temp,arr[n],check[n],var[n]={};
    for(int i=0;i<n;i++){
        cin>>temp;
        arr[i] = temp;
        check[i] = temp;
    }

    sort(arr,arr+n);

    for(int i=0;i<n;i++){
        if(arr[i]!=check[i]){
            posPrev = i;
            break;
        }
    }
    if(posPrev== -1){
        cout<<"yes"<<endl;
        cout<<1<<" "<<1<<endl;
        return 0;
    }

    for(int i=n-1;i>posPrev;i--){
        if(arr[i]!=check[i]){
            posPost=i;
            break;
        }
    }
    //cout<<posPrev<<endl;
    //cout<<posPost<<endl;

    //reverse the segment
    for(int i=posPost;i>=posPrev;i--){
        var[posPost-i] = check[i];
    }

    for(int i=posPrev;i<=posPost;i++){
        check[i] = var[i-posPrev];
    }

    for(int i=0;i<n;i++){
        if(arr[i]!=check[i]){
            cout<<"no"<<endl;
            return 0;
        }
    }

    cout<<"yes"<<endl;
    cout<<posPrev+1<<" "<<posPost+1<<endl;

}
