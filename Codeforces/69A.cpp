#include<bits/stdc++.h>

using namespace std;


int main(){

    int x,y,z,sumx=0,sumy=0,sumz=0;

    int n;
    cin>>n;

    while(n){
        cin>>x>>y>>z;
        sumx+=x;
        sumy+=y;
        sumz+=z;
        n--;
    }

    if(sumx==0 && sumy==0 && sumz==0)
        cout<<"YES"<<endl;
    else
        cout<<"NO"<<endl;


    return 0;
}
