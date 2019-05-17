/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/


class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> log = new HashMap<>();
        int result = 0, j = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (log.containsKey(s.charAt(i))) {
                j = Math.max(j, log.get(s.charAt(i)) + 1);
            }
            log.put(s.charAt(i), i);
            result = Math.max(result, i - j + 1);
        }
        return result;
    }
}

