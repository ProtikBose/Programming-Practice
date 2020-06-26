// O(n) time complexity


int Solution::maxSubArray(const vector<int> &A) {
    int max_so_far=A[0];
    int max_to_ending=0;
    
    for(int i=0;i<A.size();i++){
        max_to_ending=max_to_ending+A[i];
        
        //;
        if(max_so_far<max_to_ending)
            max_so_far=max_to_ending;
        if(max_to_ending<0) max_to_ending=0;
    }
    return max_so_far;
}