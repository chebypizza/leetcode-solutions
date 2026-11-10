class Solution {
public:
        vector<vector<int>> ans;
        vector<int> subSet;

        void backtrack(int index, int curSum, vector<int>& candidates, int target)
        {
            if (index >= candidates.size()) return;
            if (curSum > target) return;
            if (curSum == target)
            {
                ans.push_back(subSet);
                return;
            }

            subSet.push_back(candidates[index]);
            backtrack(index, curSum + candidates[index], candidates, target);

            subSet.pop_back();
            backtrack(index + 1, curSum, candidates, target);
        }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        backtrack(0, 0, candidates, target);
        return ans;
    }
};