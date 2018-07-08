"""
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.

For example, 12321 is a palindrome.



Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101


Note:

1 <= N <= 10^8
"""


class Solution:
    def primePalindrome(self, N):
        """
        :type n: int
        :rtype: int
        """
        search = True
        n = N
        while search:
            if int(n) > 1000:
                num = str(n)
                len_n = len(num)
                if len_n % 2 == 0:
                    while len_n % 2 == 0:
                        fhalf = str(num)[:len_n // 2]
                        n = int(fhalf + fhalf[::-1])
                        if self.isPrime(n) and n > N:
                            return n
                        n = num = (str(int(fhalf)+1)+str(int(fhalf))[::-1])
                        len_n = len(num)
                        # print("even",num)
                else:
                    while len_n % 2 != 0:
                        loc = len_n // 2
                        fhalf = str(num)[:loc]

                        n = int(fhalf + num[loc] + str(fhalf)[::-1])
                        if self.isPrime(n) and n > N:
                            return n
                        n = num = (str(int(fhalf)*10+int(num[loc])+1) + fhalf[::-1])
                        len_n = len(num)
                        # print("odd",num)

            else:
                while not self.isPalindrome(n):
                    n += 1
                if self.isPrime(n):
                    return n
                n += 1

    def isPrime(self, x):
        if x >= 2:
            for y in range(2, x):
                if not (x % y):
                    return False
        else:
            return False
        return True

    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        return False


x = Solution().primePalindrome(3503054)
print(x)