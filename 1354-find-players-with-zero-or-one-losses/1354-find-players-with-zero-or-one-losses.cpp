class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int,int>loser_count;
        for(int i=0;i<matches.size();i++){
            int loser=matches[i][1];
            loser_count[loser]++;
        }
        vector<int>never_lost;
        vector<int>lost_once;
        for(int i=0;i<matches.size();i++){
            int winner=matches[i][0];
            int loser=matches[i][1];
            if(loser_count.find(winner)==loser_count.end()){
            never_lost.push_back(winner);
            loser_count[winner]=2;
            }
            if(loser_count[loser]==1){
                lost_once.push_back(loser);
            }
        }
        sort(begin(never_lost),end(never_lost));
        sort(begin(lost_once),end(lost_once));

        return {never_lost,lost_once};
    }
};