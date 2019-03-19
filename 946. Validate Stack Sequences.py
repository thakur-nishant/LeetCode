"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        i = 0
        while i < len(pushed) and j < len(popped):
            # print(stack, i ,j)
            # print("#####",pushed[i],popped[j])
            if pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                i += 1
                j += 1
                # print(stack[-1], popped[j])
                while stack and j < len(popped) and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1

        if stack or i < len(pushed) or j < len(popped):
            return False

        return True


