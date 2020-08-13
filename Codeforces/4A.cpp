#include<bits/stdc++.h>

using namespace std;

int main()
{
    int w;
    cin>>w;
    string output;
    if(w<=2)
    {
        output="NO";
    }
    else if(w%2)
    {
        output="NO";
    }
    else
        output="YES";
    cout<<output<<endl;

    return 0;
}
