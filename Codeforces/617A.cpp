#include<bits/stdc++.h>

using namespace std;


int main(){

    int counting=0,x;
    cin>>x;

    if(x<=5) counting=1;
    else{
        while(x){
            if(5<=x){
                x=x-5;
                counting++;
            }
            else if(4<=x){
                x=x-4;
                counting++;
            }
            else if(3<=x){
                x=x-3;
                counting++;
            }
            else if(2<=x){
                x=x-2;
                counting++;
            }
            else if(1<=x){
                x=x-1;
                counting++;
            }
        }
    }
    cout<<counting<<endl;

    return 0;
}
