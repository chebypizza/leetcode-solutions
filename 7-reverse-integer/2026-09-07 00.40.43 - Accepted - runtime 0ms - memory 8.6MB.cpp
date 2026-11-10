class Solution {
public:
    int reverse(int x) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        long long sX = x;
        long long ans = 0;

        while (sX != 0){
            ans = ans * 10 + (sX % 10);
            sX /= 10;
        }

        if (ans < INT_MIN || ans > INT_MAX){
            return 0;
        }

        return ans;
    }
};