class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        std::vector<int> ans;
        int low = 0;
        int high = arr.size();

        while (low < high){
            int mid = (low + high) / 2;

            if (arr[mid] < x){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }

        int left = low - 1;

        while (ans.size() != k){
            if (left < 0){
                ans.push_back(arr[low]);
                low++;
            }
            else if (low == arr.size()){
                ans.push_back(arr[left]);
                left--;
            }
            else if (std::abs(arr[left] - x) <= std::abs(arr[low] - x)){
                ans.push_back(arr[left]);
                left--;
            }
            else{
                ans.push_back(arr[low]);
                low++;
            }
        }

        std::sort(ans.begin(), ans.end());

        return ans;
    }
};