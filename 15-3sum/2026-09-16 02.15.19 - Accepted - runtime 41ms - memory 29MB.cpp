class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector <int>> ans;
        int n = nums.size();

        for(int i = 0; i < n; i++)
        {
            if (nums[i] > 0)
            {
                break;
            }

            if (i != 0 && nums[i] == nums[i - 1])
            {
                continue;
            }

            int left = i + 1;
            int right = n - 1;

            while (left < right)
            {
                int curSum = nums[i] + nums[left] + nums[right];

                if (curSum == 0)
                {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    left += 1;
                    right -=1;

                    while(left < right && nums[left] == nums[left - 1])
                    {
                        left += 1;
                    }
                    while(left < right && nums[right] == nums[right + 1])
                    {
                        right -= 1;
                    }
                }

                else if(curSum > 0)
                {
                    right -= 1;
                }
                else
                {
                    left += 1;
                }
            }
        }

        return ans;
    }
};