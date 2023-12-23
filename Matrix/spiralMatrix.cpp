// 54) Spiral Matrix

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();

        if (m == 0) return {};

        int n = matrix[0].size();
        if (n == 0) return {}; 

        vector<vector<int>> dir { {0, -1}, {0, 1}, {1, 0}, {-1, 0}}; 
        vector<int> res; 

        int N = m * n;
        int d = 0, i = 0, j = -1; 

        while (res.size() < N) {
            int ni = i + dir[d][0];
            int nj = j + dir[d][1]; 

            while (ni < 0 || ni >= m || nj < 0 || nj >= n || matrix[ni][nj] == INT_MIN) {
                d = (d + 1) % 4; 
                ni = i + dir[d][0];
                nj = j + dir[d][1]; 

            }
            res.push_back(matrix[ni][nj]);
            matrix[ni][nj] = INT_MIN;
            i = ni;
            j = nj;

        }

        return res; 
    }
};
