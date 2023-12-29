// 52 - N-Queens II
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int sols; 
    int totalNQueens(int n) {
        if (n == 1) return 1;
        vector<int> queens = vector<int>();
        sols = backtrack(queens, 0, n);
        return sols;
    }

    int backtrack(vector<int>& s, int curr_row, int n) {
        if (isSolution(s, n)) {
            sols += 1;
        }

        vector<int> candidates = vector<int>();
        if (construct(s, curr_row, n, candidates)) {
            for (size_t i=0; i<candidates.size(); ++i) {
                s.push_back(candidates[i]);
                backtrack(s, curr_row+1, n);
                s.pop_back();
            }
        }

        return sols;
    }

    bool isSolution(const vector<int>& s, int n) {
        return (s.size() == n);

    }

    bool isSquareSafe(const vector<int>& s, int r, int c) {
        // (r, c) = (row, col) check if square is safe for queen to be
        for (int i=0; i < s.size(); ++i) {
            if (i == r || s[i] == c) return false;
            if (abs(i-r) == abs(s[i]-c)) return false;
        }
        return true; 
    }

    bool construct(const vector<int>& s, int row, int n, vector<int>& candidates) {
        for (int i=0; i<n; ++i) {
            if (isSquareSafe(s, row, i)) candidates.push_back(i);

        }
        return candidates.size() > 0;
    }

};
