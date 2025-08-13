class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n=nums.size(),f=-1;
        for(int i=0;i<n;i++){
            if(nums[i]==target){
                f=i;
                break;
            }}
        if(f>-1)
          return f;
        else
          return f;
    }
};