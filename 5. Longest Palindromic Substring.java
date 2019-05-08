/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
 */

class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) return "";
        String result = "", odd, even;
        for (int i = 0; i < s.length(); ++i) {
            odd = expandAroundCenter(s,i,i);
            if (odd.length() > result.length()) result = odd;
            even = expandAroundCenter(s, i, i+1);
            if (even.length() > result.length()) result = even;
        }
        return result;
    }

    public String expandAroundCenter(String s, int i,int j) {
        while (i >= 0  && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        return s.substring(i+1,j);
    }
}
