class Solution {
public:
    char findTheDifference(string s, string t) {
        int sum_s=0;
        for(char &ch:s){
            sum_s=sum_s+ch;
        }
        int sum_=0;
        for(char &ch:t){
            sum_=sum_+ch;
        }
        return sum_-sum_s;
    }
};