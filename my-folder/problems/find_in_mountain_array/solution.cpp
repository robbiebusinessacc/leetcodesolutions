/**
 * This is MountainArray's API interface.
 * You should not implement it, or speculate about its implementation
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int length = mountainArr.length();
        int low = 0, high = length - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        int peak_index = low;

        int increasing_index = binary_search(0, peak_index, target, mountainArr, false);
        if (mountainArr.get(increasing_index) == target) {
            return increasing_index;
        }
        int decreasing_index = binary_search(peak_index + 1, length - 1, target, mountainArr, true);
        if (mountainArr.get(decreasing_index) == target) {
            return decreasing_index;
        }

        return -1;
    }

private:
    int binary_search(int low, int high, int target, MountainArray &mountainArr, bool isReversed) {
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (isReversed) {
                if (mountainArr.get(mid) > target) {
                    low = mid + 1;
                } else {
                    high = mid;
                }
            } else {
                if (mountainArr.get(mid) < target) {
                    low = mid + 1;
                } else {
                    high = mid;
                }
            }
        }
        return low;
    }
};
