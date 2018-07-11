"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""
"""
A faster solution
"""

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in [2,3,5]:
            while num % i == 0 and num:
                num = num // i

        return num == 1


"""Solution little slower"""
# class Solution:
#     def isUgly(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 0:
#             return False
#         facts = set()
#         i = 2
#         while i <= num:
#             if self.isPrime(num):
#                 facts.add(num)
#                 num = num // num
#             else:
#                 while num % i == 0:
#                     facts.add(i)
#                     num = num // i
#             i += 1
#
#         print(facts)
#         if facts - {2, 3, 5}:
#             return False
#         return True
#
#     def isPrime(self,num):
#         for i in range(2,int(num**0.5)+2):
#             if num % i == 0:
#                 return False
#         return True

""" Slowest solution """
# class Solution:
#     def isUgly(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 0:
#             return False
#
#         map_facts = {}
#         for n in range(1, num + 1):
#             facts = self.getFactors(n, map_facts)
#             map_facts[n] = facts
#
#         print(map_facts)
#
#         if map_facts[num] - {1, 2, 3, 5}:
#             return False
#         return True
#
#     def getFactors(self, num, map_facts):
#         facts = set()
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 if i in map_facts:
#                     for n in map_facts[i]:
#                         facts.add(n)
#                 else:
#                     facts.add(i)
#
#         if len(facts) <= 2:
#             return facts
#         return facts - {num}




x = Solution().isUgly(14)
print(x)
