/*
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

*/
class NumArray {

    int[] sums;

    public NumArray(int[] nums) {
        sums = new int[nums.length + 1];
        for (int i = 1; i < sums.length; ++i) {
            sums[i] = sums[i-1] + nums[i-1];
        }
    }

    public int sumRange(int i, int j) {
        return sums[j+1] - sums[i];
    }
}

class NumArray {

    int[] numsArray;

    public NumArray(int[] nums) {
        // numsArray = new int[nums.length];
        numsArray = nums;
    }

    public int sumRange(int i, int j) {
        int result = 0;
        for (int k = i; k <= j; ++k) {
            result = result + numsArray[k];
        }
        return result;
    }
}

class NumArray {

    private List<Integer> numArray = new ArrayList<Integer>();

    public NumArray(int[] nums) {
        numArray.clear();
        for (int i=0; i <nums.length; ++i) {
            numArray.add(nums[i]);
        }
    }

    public int sumRange(int i, int j) {
        int result = 0;
        for (int k = i; k <= j; ++k) {
            result = result + numArray.get(k);
        }
        return result;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
