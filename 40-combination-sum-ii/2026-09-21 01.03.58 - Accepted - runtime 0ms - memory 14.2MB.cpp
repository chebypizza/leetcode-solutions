class Solution {
public:
    std::vector<std::vector<int>> ans;
    std::vector<int> subset;

    void backtrack(int index, int curSum, std::vector<int>& candidates, int target)
    {
        if (curSum == target)
        {
            ans.push_back(subset);
            return;
        }

        if (index >= candidates.size() || curSum > target)
        {
            return;
        }

        subset.push_back(candidates[index]);
        backtrack(index + 1, curSum + candidates[index], candidates, target);

        subset.pop_back();

        while (index + 1 < candidates.size() && candidates[index] == candidates[index + 1])
        {
            index++;
        }

        backtrack(index + 1, curSum, candidates, target);
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        std::sort(candidates.begin(), candidates.end());
        
        backtrack(0, 0, candidates, target);
        return ans;
    }
};