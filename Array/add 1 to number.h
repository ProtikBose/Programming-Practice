// O(n) time complexity

vector<int> Solution::plusOne(vector<int> &A) {
    
    int map=0;
    vector<int>result;
    for(int i=A.size()-1;i>=0;i--){
        if(i==A.size()-1){
            if(A[i]==9){
                A[i]=0;
                result.push_back(A[i]);
                map=1;
            }
            else{
                A[i]=A[i]+1;
                result.push_back(A[i]);
            }
        }
        
        else{
            if(map==1){
                if(A[i]==9){
                    A[i]=0;
                    result.push_back(A[i]);
                    map=1;
                }
                else{
                    A[i]=A[i]+1;
                    result.push_back(A[i]);
                    map=0;
                }
            }
            else{
               result.push_back(A[i]); 
            }
        }
        if(i==0 && map==1) result.push_back(map);
    }
    while(result[result.size()-1]==0) result.pop_back();
    reverse(result.begin(),result.end());
    return result;
}
