class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        std::unordered_set<int> newSet;

        for(int right = 0; right < nums.size(); right++){
            if (right > k){
                newSet.erase(nums[right - k - 1]);
            }

            if (newSet.count(nums[right])){
                return true;
            }

            newSet.insert(nums[right]);
        }

        return false;
    }
};