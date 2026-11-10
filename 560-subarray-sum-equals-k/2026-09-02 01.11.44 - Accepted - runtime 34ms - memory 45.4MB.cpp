class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int>dictSeen;
        int count = 0;
        int curSum = 0;
        int n = nums.size();
        dictSeen[0] = 1;

        for (int i = 0; i < n; i++) {                      //curSum - k = targetCurSum
            curSum += nums[i];
            if (dictSeen.find(curSum - k) != dictSeen.end()){
                count += dictSeen[curSum - k];
            }
            dictSeen[curSum]++;
        }

        return count;
    }
};