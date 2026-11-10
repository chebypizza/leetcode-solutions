class Solution {
private:
    std::vector<std::vector<int>> ans;
    std::vector<int> subset;

    void backtrack(int index, const std::vector<int>& nums){
        if (index == nums.size()){
            ans.push_back(subset);
            return;
        }

        subset.push_back(nums[index]);
        backtrack(index + 1, nums);

        subset.pop_back();

        backtrack(index + 1, nums);
    }
    
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums){
        ans.clear();
        subset.clear();

        backtrack(0, nums);
        return ans;
    }
};