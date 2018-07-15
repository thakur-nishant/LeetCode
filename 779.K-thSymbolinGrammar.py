"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        grammar = {}
        grammar["0"] = "01"
        grammar["1"] = "10"
        if K == 1:
            return 0
        else:
            getList = []
            while K != 1:
                if K % 2:
                    getList.append(0)
                    K = (K + 1) // 2
                else:
                    getList.append(1)
                    K = K // 2
            cur = "0"
            print(getList)
            for i in range(len(getList)):
                cur = grammar[cur][getList[-i-1]]
            return int(cur)


"""
######################### Method 1 ###############################

class Solution(object):
    def kthGrammar(self, N, K):
        record = {1: '0'}

        row = 2
        while row <= N:
            val = ""
            for i in record[row - 1]:
                if i == '0':
                    val += '01'
                else:
                    val += '10'
            record[row] = val
            row += 1

        for i in range(1, N+1):
            print(record[i])

        return int(record[N][K - 1])
        
        
######################## Method 2 #######################
class Solution(object):
    def kthGrammar(self, N, K):
        count = 2
        result = "0"
        while count <= N:
            if count%2 != 0:
                result += result[::-1]
            else:
                invert = ""
                for i in result:
                    if i == '0':
                        invert += '1'
                    else:
                        invert += '0'
                result += invert
            print(count,result)
            count += 1
        return int(result[K - 1])

"""



x = Solution().kthGrammar(30,434991989)
print(x)