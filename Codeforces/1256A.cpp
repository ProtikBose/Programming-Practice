#include<bits/stdc++.h>

using namespace std;

int main()
{

    long long int q,a,b,n,s;
    cin>>q;

    while(q)
    {
        cin>>a>>b>>n>>s;

        if(n==s || b==s)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            long long int var=s/n;
            if(var<=a)
            {
                long long int res=s-(var*n);


                if(res<=b)
                    cout<<"YES"<<endl;
                else
                {
                    cout<<"NO"<<endl;
                }
            }
            else
            {
                long long int res=s-(a*n);


                if(res<=b)
                    cout<<"YES"<<endl;
                else
                {
                    cout<<"NO"<<endl;
                }
            }
        }
        q--;




    }
    return 0;
}
