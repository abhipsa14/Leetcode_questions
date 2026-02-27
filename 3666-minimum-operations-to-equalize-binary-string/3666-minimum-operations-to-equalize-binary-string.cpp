class Solution {
public:
    int minOperations(string s, int k) {
        int n=s.length();
        int startZeros=0;
        for(char &ch: s){
            if(ch=='0')
               startZeros++;
        }
        if(startZeros==0){
            return 0;
        }
        vector<int> oper(n+1,-1);
        set<int>evenSet;
        set<int>oddSet;
        for(int count=0;count<=n;count++){
            if(count%2==0){
                evenSet.insert(count);
            }
            else{
                oddSet.insert(count);
            }
        }
        queue<int>que;
        que.push(startZeros);
        oper[startZeros]=0;
        if(startZeros%2==0){
            evenSet.erase(startZeros);
        }else{
            oddSet.erase(startZeros);
        }
        while(!que.empty()){
            int z=que.front();
            que.pop();
            int min_new_z=z+k-2*min(k,z);
            int max_new_z=z+k-2*max(0,k-n+z);

            set<int> &currSet=(min_new_z%2==0)?evenSet:oddSet;
            auto it=currSet.lower_bound(min_new_z);
            while(it!=currSet.end() && *it<=max_new_z){
                int newz=*it;
                if(oper[newz]==-1){
                    oper[newz]=oper[z]+1;
                    if(newz==0){
                        return oper[newz];
                    }
                    que.push(newz);
                }
                it=currSet.erase(it);
            }
        }
        return -1;
    }
};