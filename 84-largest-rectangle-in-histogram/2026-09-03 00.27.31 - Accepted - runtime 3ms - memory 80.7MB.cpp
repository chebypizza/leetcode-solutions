class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {

        heights.push_back(0);

        int n = heights.size();
        int maxAns = 0;

        vector<int> stack;
        stack.reserve(n);

        for (int i = 0; i < n; i++){
            while (!stack.empty() && heights[stack.back()] > heights[i]){
                int last = stack.back();
                stack.pop_back();
                int height = heights[last];
                int width;

                if (!stack.empty()) {
                    width = i - stack.back() - 1;
                }
                else{
                    width = i;
                }

                maxAns = std::max(maxAns, width * height);
            }
            stack.push_back(i);
        }

        return maxAns;
    }
};