class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int z = 0; z < nums.length; z++) {
                if (i != z) {
                    if (nums[i] + nums[z] == target) {
                        int[] x = {i,z};
                        return x;
                    }
                }
            }
        }
        return null;
    }
}