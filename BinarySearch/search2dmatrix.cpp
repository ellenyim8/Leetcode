// 74) Search a 2D Matrix
#include <vector>
#include <iostream>
using namespace std; 

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size(); 

        for (int j=0; j < n; j++) {
            for (int i=0; i < m; i++) {
                if (matrix[j][i] == target) {
                    return true; 
                }
            }
        }

        return false; 
    }
};

