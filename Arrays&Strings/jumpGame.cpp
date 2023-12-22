// 55) Jump Game

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int jmp = 0, n = nums.size(); 

        for (int i=0; i<n; ++i) {
            if (i <= jmp) {
                jmp = max(i + nums[i], jmp);

            }else {
                break; 
            }
        }

        return jmp >= n - 1; 
    }
};
