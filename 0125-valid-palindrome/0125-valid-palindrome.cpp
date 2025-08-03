class Solution {
public:
    bool isPalindrome(string s) {
     string s1="";
     for(char n:s){
        if(isalnum(n)){
            s1+=tolower(n);
        }
     }
     int left=0;
     int right=s1.size()-1;
     while(left<=right){
        if(s1[left]!=s1[right])return false;
        left++;
        right--;
     }
     return true;
     
    }
};