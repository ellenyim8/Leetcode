// 274) H-Index

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());

        int h = citations.size();

        int st = 0, end = h - 1;

        int cnt = 0;

        while (st <= end) {
            int mid = st + (end - st) / 2;

            if (citations[mid] >= h - mid) {
                cnt = max(cnt, h - mid);
                end = mid - 1;
            }
            else {
                st = mid + 1;
            }
        }
        return cnt;

    }
};
