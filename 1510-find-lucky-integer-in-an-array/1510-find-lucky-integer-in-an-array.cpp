class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int>mp;
        int max_int=0;
        for (int a:arr){
            mp[a]++;
        }
        for(auto i: mp){
            if(i.second==i.first){
                max_int=max(max_int,i.first);
            }
        }
        if(max_int>0)return max_int;
        else return-1;
    }
};