class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int ind=-1;
        int n=nums.size();
        int i=n-2;
        for(;i>=0;i--){
            if(nums[i]<nums[i+1]){
                ind=i;
                break;
            }
        }
         if (ind == -1) {
            reverse(nums.begin(), nums.end());
            return;
        }

        for(int j=n-1;j>=0;j--){
           if(nums[j]>nums[ind]){
            swap(nums[j],nums[ind]);
            break;
           }
        }
        reverse(nums.begin()+ind+1,nums.end());
    
    }
};