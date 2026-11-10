class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int curSum = 0;
        int left = 0;
        int n = nums.size();
        int bestQuantity = n + 1;

        for(int right = 0; right < n; right++){
            curSum += nums[right];
            while(curSum >= target){
                bestQuantity = std::min(right - left + 1, bestQuantity);
                curSum -= nums[left];
                left += 1;
            }
        }

        if (bestQuantity <= n){
            return bestQuantity;
        }

        return 0;
    }
};