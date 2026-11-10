class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *std::max_element(piles.begin(), piles.end());

        while (left <= right){
            long long hours = 0;
            int mid = (left + right) / 2;

            for (const int& pile : piles){
                hours += (pile + mid - 1) / mid;
            }

            if (hours <= h){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }

        return left;
    }   
};