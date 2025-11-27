class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalg=0,totalc=0,n=gas.size(),idx=0,currg=0;
        for(int i=0;i<n;i++){
            totalg+=gas[i];
            totalc+=cost[i];
            currg+=gas[i];
            currg-=cost[i];
            if(currg<0){
                currg=0;
                idx=i+1;
            }
        }
        return totalg>=totalc?idx:-1;
    }
};