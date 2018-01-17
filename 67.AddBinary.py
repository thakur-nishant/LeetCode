class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)
        n2 = len(b)

        if n1 > n2:
            b = '0' * (n1 - n2) + b
        else:
            a = '0' * (n2 - n1) + a

        # print(a,b)
        carry = 0
        ans = ''

        for i in range(len(a) - 1, -1, -1):
            if int(a[i]) and int(b[i]):
                # print('case 1')
                if carry:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                carry = 1
            elif int(a[i]) or int(b[i]):
                # print('case 2')
                if carry:
                    ans = '0' + ans
                    carry = 1
                else:
                    ans = '1' + ans
                    carry = 0
            else:
                # print('case 3')
                if carry:
                    ans = '1' + ans
                    carry = 0
                else:
                    ans = '0' + ans
                    carry = 0


        if carry:
            return str(carry) + ans
        else:
            return ans


test = Solution()

x = test.addBinary('11','1')
print(x)

