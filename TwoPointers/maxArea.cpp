// 11) Container with most water 
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1, res = 0; 

        while (left < right) {
            res = max(res, min(height[left], height[right]) * (right - left)); 
            height[left] < height[right] ? left += 1 : right -= 1; 

        }

        return res; 
    }
};

