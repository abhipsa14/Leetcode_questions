class Solution {
public:
    int maxProduct(vector<int>& nums) {
       int n=nums.size();
       int maxproduct=INT_MIN;
       int lefttoright=1;
       int righttoleft=1;
       for(int i=0;i<n;i++){
        if(lefttoright==0){
            lefttoright=1;
        }
        if(righttoleft==0){
            righttoleft=1;
        }
        lefttoright*=nums[i];
        int j=n-i-1;
        righttoleft*=nums[j];
        maxproduct=max({maxproduct,lefttoright,righttoleft});
       }
       return maxproduct;
    }
};