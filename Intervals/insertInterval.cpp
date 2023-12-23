// 57) Insert Interval 

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> its; 

        // intervals: [[1,3], [6,9]]
        // newInterval: [2,5] 

        // output: 1 <= 2 <= 3; 5 <= 6
        // [[1,5], [6,9]]
        int new_start = newInterval[0];
        int new_end = newInterval[1];
        vector<vector<int > > new_intervals; 
        bool insertedInterval = false;

        for (int i=0; i<intervals.size(); i++ ) {
            
            if (intervals[i][1] < new_start) {
                new_intervals.push_back(intervals[i]); 
            }
            else if (intervals[i][0] > new_end) {
                if (!insertedInterval) {
                    new_intervals.push_back(newInterval);
                    insertedInterval = true; 
                }
                new_intervals.push_back(intervals[i]); 
            }
            else {
                newInterval[0] = min(newInterval[0], intervals[i][0]);
                newInterval[1] = max(newInterval[1], intervals[i][1]);
            }

        }

        if (!insertedInterval) {
            new_intervals.push_back(newInterval);
        }

        return new_intervals;
        

        // Time Complexity: O(n)
        // Space Complexity: O(n) 
    }
};

