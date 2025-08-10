class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int>mp;
        int m=nums[0];
        for(int n:nums){
            mp[n]++;
        }
        for(auto n:mp){
            if(n.second>1){
               m=n.first;
            }
        }
        return m;
    }
};