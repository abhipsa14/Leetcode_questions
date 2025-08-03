class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());
        int max_len = 0;

        for (int num : num_set) {
            // Check if it's the start of a sequence
            if (num_set.find(num - 1) == num_set.end()) {
                int current_num = num;
                int current_streak = 1;

                // Count sequence length
                while (num_set.find(current_num + 1) != num_set.end()) {
                    current_num++;
                    current_streak++;
                }

                max_len = max(max_len, current_streak);
            }
        }

        return max_len;
    }
};
