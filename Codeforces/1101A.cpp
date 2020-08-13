#include<bits/stdc++.h>

using namespace std;


int main(){

    long long int q,l,r,val,result;

    cin>>q;

    while(q){
        cin>>l>>r>>val;
        result=0;
        if(val>=l){
            if(val>r){
                result=val*1;
            }
            else{
                if(!(r%val)){
                    result=val*((r/val)+1);
                }
                else{
                    result=val*(((r-(r%val))/val)+1);
                }
            }
        }
        else{
            result=val*1;
        }

        cout<<result<<endl;
        q--;
    }


    return 0;
}
