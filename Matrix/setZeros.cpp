// 73) Set Matrix Zeros

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool setRow = false, setCol = false; 
        int m = matrix.size(), n = matrix[0].size(); 

        for (int j=0; j<n; j++) {
            if (matrix[0][j] == 0) {
                setRow = true; 
                break; 
            }
        }

        for (int i=0; i<m; i++) {
            if (matrix[i][0] == 0) {
                setCol = true;
                break; 

            }
        }

        for (int i=1; i<m; i++ ) {
            for (int j=1; j<n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0; matrix[0][j] = 0; 
                }
            }
        }

        for (int i=1; i<m; i++) {
            for (int j=1; j<n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0; 
                }
            }
        }

        if (setRow) {
            for (int j=0; j<n; j++) {
                matrix[0][j] = 0; 
            }
        }

        if (setCol) {
            for (int i=0; i<m; i++) {
                matrix[i][0] = 0; 
            }
        }

    }
};

