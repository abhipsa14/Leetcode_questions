class Solution {
public:
    int maxSum(vector<int>& nums) {
        // unordered_set<int> st;
        vector<int>st(101,-1);
        int sum=0;
        int maxneg=INT_MIN;
        for(int &num:nums){
          if(num<=0) maxneg=max(maxneg,num);
          else if(st[num]==-1){
             sum+=num;
             st[num]=1;
          }
    }
    return sum==0?maxneg:sum;
    }
};