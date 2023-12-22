// 27) Remove Element

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int right = nums.size() - 1, n = nums.size(), count = n; 

        for (int i=0; i<n && i <= right; ++i) {
            while (right >= 0 &&   nums[right] == val ) {
                --right; 
                --count; 
            }
            if (nums[i] == val && i <= right) {
                swap(nums[i], nums[right--]); 
                --count; 
            }
        }
        return count; 
    }
};