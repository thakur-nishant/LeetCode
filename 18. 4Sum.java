/*
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
 */


class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        ArrayList<List<Integer>> results = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        ArrayList<Integer> result = new ArrayList<Integer>();
        findNSum(0, nums.length-1, nums, target, 4, result, results);
        return results;
    }

    public void findNSum(int l, int r, int[] nums, int target, int N, List<Integer> result, List<List<Integer>> results) {
        if (N < 2 || r-l+1 < N || target < nums[l]*N || target > nums[r]*N)
            return;
        if(N == 2) {
            ArrayList<Integer> currList;
            int temp;
            while (l<r) {
                temp = nums[l]+nums[r];
                if (temp == target) {
                    currList = new ArrayList<Integer>();
                    currList.addAll(result);
                    currList.add(nums[l]);
                    currList.add(nums[r]);
                    results.add(currList);
                    l++;
                    while (l<r && nums[l] == nums[l-1]) l++;
                }
                else if (temp<target) l++;
                else r--;
            }
        } else {
            for(int i = l; i <= r; ++i) {
                ArrayList<Integer> currRes;

                if (i==l || (i>l && nums[i] != nums[i-1])){
                    currRes = new ArrayList<Integer>();
                    currRes.addAll(result);
                    currRes.add(nums[i]);
                    findNSum(i+1, r, nums, target-nums[i], N-1, currRes, results);
                }
            }
        }
    }
}