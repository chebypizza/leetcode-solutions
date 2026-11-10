class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int generalSum = std::accumulate(nums.begin(), nums.end(), 0);
        int curSum = 0;

        for(int i = 0; i < nums.size(); ++i){
            if (curSum * 2 + nums[i] == generalSum){
                return i;
            }

            curSum += nums[i];
        }

        return -1;
    }
};