// 3) Longest Substring without Repeating Characters

#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> substr; 
        int ret = 0, slow = 0, n = s.size();
        for (int fast=0; fast<n; ++fast) {
            if (substr.count(s[fast]) != 0) {
                slow = max(slow, substr[s[fast]] + 1); 
            }
            substr[s[fast]] = fast; 
            ret = max(ret, fast - slow + 1); 
        }
        return ret;

        // int n = s.length()-1;
        // int dp[n+1];
        // for (int i=0; i<n; i++) {
        //     dp[i] = 1; 
        // }

        // for (int i=1; i < n; i++) {
        //     for (int j=0; j<i-1; j++) {
        //         if (s[i] != s[j] && dp[i] < dp[j] + 1) {
        //             dp[i] = dp[j] + 1;
        //         }
        //     }
        // }

        // int longest = dp[1];
        // for (int i=1; i<n; i++) {
        //     if (dp[i] > longest) {
        //         longest = max(longest, dp[i]);
        //     }
        // }

        // return longest; 
    }
};
