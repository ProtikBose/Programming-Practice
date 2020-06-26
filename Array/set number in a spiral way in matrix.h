// O(R*C) time complexity

vector<vector<int> > Solution::generateMatrix(int A) {
    
    vector<vector<int> > sol(A,vector<int>(A));
 int d= 1;
int start =0;
//the way a human would fill this-->
//print every square, starting with the outermost 
//start is the distance from boundry which is 0 for first square
while(d<=A*A){
    
    //top side
    for(int i=start; i<(A-start);i++){
        sol[start][i]=d;
        d++;
    }
    //right side
    for(int i=start+1; i<(A-start);i++){
        sol[i][A-start-1]=d;
        d++;
    }
    //bottom side
    for(int i=A-start-2; i>=start;i--){
        sol[A-start-1][i]=d;
        d++;
    }
    //left side
    for(int i=A-start-2; i>start;i--){
        sol[i][start]=d;
        d++;
    }
    //next square
    start++;
}
return sol;

}
