// 35) Search Insert Position
#include <vector>
#include <iostream>
using namespace std; 

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int first=0, last=nums.size()-1; 

        while (first <= last) {
            int middle = first + (last - first) / 2; 
            if (nums[middle] == target) {
                return middle; 
            }
            else if (nums[middle] > target) {
                last = middle - 1; 
            } 
            else {
                first = middle + 1; 
            }
        }

        return first; 
    }
};

