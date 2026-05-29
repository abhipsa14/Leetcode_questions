class Solution {
public:
    int sum(int n){
        int a=0;
        int s=0;
        while(n>0){
            a=n%10;
            s+=a;
            n=n/10;
        }
        return s;
    }
    int minElement(vector<int>& nums) {
        int m=nums.size();
        for(int i=0;i<m;i++){
            nums[i]=sum(nums[i]);
        }
        sort(nums.begin(),nums.end());
        return nums[0];
    }
};