class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left = 0;
        int right = 0;

        for (int weight : weights){
            if (weight > left){
                left = weight;
            }
            right += weight;
        }

        while (left <= right){
            int generalWeight = 0;
            int daysNeeded = 1;
            int mid = (left + right) / 2;

            for (const int& weight : weights){
                generalWeight += weight;
                if (generalWeight > mid){
                    daysNeeded += 1;
                    generalWeight = weight;
                }
            }

            if (daysNeeded <= days){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }

        }
        
        return left;
    }
};