#include <algorithm> 
#include <string>
using namespace std; 

class Solution {
public:
    int minDistance(string word1, string word2) {
        int dist = 0; 

        int x = word1.length(); 
        int y = word2.length(); 

        int dp[x+1][y+1]; 
        dp[0][0] = 0; 
        //int insert = 0, remove = 0, edit = 0; 
        for (int i=0; i<=x; i++) {
            for (int j=0; j<=y; j++) {
                if (i == 0 && j > 0) {
                    dp[0][j] = dp[0][j-1] + 1; 
                }
                else if (i > 0 && j == 0) {
                    dp[i][0] = dp[i-1][0] + 1; 
                }
                else if (i > 0 && j > 0) {
                    if (word1[i-1] == word2[j-1]) {
                        dp[i][j] = dp[i-1][j-1]; 
                    }
                    else {

                        dp[i][j] = min(min(dp[i][j-1] + 1, dp[i-1][j] + 1), dp[i-1][j-1] + 1); 
                    }
                }
            }
        }

        return dp[x][y]; 

        // word1 = horse
        // word2 = ros 
        /* 
          - r o s
        - 0 1 2 3
        h 1 2 3 4
        o 1 2 2 3
        r 1 1 2 3
        s 1 2 3 3
        e 1 2 3 4
        
        horse 
        ro-s-  replace h with r, remove r, remove e

        */
    }
};