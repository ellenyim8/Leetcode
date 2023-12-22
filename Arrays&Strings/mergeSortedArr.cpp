// 88) Merge Sorted Array 

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> temp = nums1;

        // clear out nums1
        nums1.clear();
        nums1.resize(m + n);

        int p1 = 0;
        int p2 = 0;
        int p3 = 0;
        while ((p1 < m) && (p2 < n)) {
            if (temp[p1] < nums2[p2]) {
                nums1[p3++] = temp[p1];
                p1++;
            }
            else {
                nums1[p3++] = nums2[p2];
                p2++;
            }
        }

        while (p1 < m) {
            nums1[p3++] = temp[p1];
            p1++;
        }
        while (p2 < n) {
            nums1[p3++] = nums2[p2];
            p2++;
        }

    }
};