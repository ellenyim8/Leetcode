// 53) Maximum subarray
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int max_sum = nums[0]; 

        for (int i=1; i < n; i++) {
            if (nums[i-1] > 0) nums[i] += nums[i-1]; 
            max_sum = max(max_sum, nums[i]); 
        }

        return max_sum; 
    }
};
