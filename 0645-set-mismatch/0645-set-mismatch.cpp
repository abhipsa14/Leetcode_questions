class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int>res;
        unordered_map<int,int>mp;
        for(int num:nums){
            mp[num]++;
        }
        for(auto i:mp){
            if(i.second>1){
                res.push_back(i.first);
            }
        }
        for(int i=1;i<=nums.size();i++){
            if(mp[i]==0){
                res.push_back(i);
            }
        }
        return res;
    }
};