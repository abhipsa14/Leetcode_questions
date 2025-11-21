class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        int m = original;
        set<int>s;
        for (int x : nums) {
           s.insert(x);
        }
        for(int x: s){
            if(x==m){
                m=m*2;
            }
        }
        return m;
    }
};
