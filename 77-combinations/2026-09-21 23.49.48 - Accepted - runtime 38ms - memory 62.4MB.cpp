class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> ans;
        std::vector<int> subset;

        backtrack(1, subset, n, k, ans);
        return ans;
    }

    void backtrack(int start, std::vector<int>& subset, int n, int k, std::vector<std::vector<int>>& ans)
    {
        if (subset.size() == k)
        {
            ans.push_back(subset);
            return;
        }
        
        int limit = n - (k - subset.size()) + 1;
        for (int i = start;i <= limit; i++)
        {
            subset.push_back(i);
            backtrack(i + 1, subset, n, k, ans);
            subset.pop_back();
        }
    }
};