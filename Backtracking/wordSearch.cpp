// 79) Word Search 

#include <vector>
#include <iostream>
using namespace std;
#include <string>

class Solution {
public:
    int direct[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}}; 

    bool exist(vector<vector<char>>& board, string word) {
        if (word.empty()) return true; 

        if (board.empty() || board[0].empty()) return false; 

        int m = board.size(); int n = board[0].size();
        int k = word.size();

        for (int i=0; i<m; ++i) {
            for (int j=0; j<n; ++j) {
                if (backtrack(board, word, i, j, 0)) 
                    return true; 
            }
        }
        return false; 
    }

    bool backtrack(vector<vector<char>>& board, string word, int i, int j, int k) {
        int m =board.size(), n = board[0].size(), sz=word.size();
        if (board[i][j] != word[k] ) return false; 

        if (k == sz - 1) return true; 

        board[i][j] = '#';
        for (int d=0; d < 4; ++d) {
            int ni = i + direct[d][0], nj = j + direct[d][1];
            if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue; 
            if (backtrack(board, word, ni, nj, k+1)) return true; 
        }
        board[i][j] = word[k]; 
        return false; 
    }

};
