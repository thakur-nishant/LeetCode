"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not wordList:
            return []
        wordList = set(wordList)
        result = []
        queue = [(beginWord, [], set())]
        while queue:
            curr, curr_list, visited = queue.pop(0)
            curr_list = curr_list + [curr]
            visited.add(curr)
            if curr == endWord:
                if not result:
                    result.append(curr_list)
                else: 
                    if len(curr_list) <= len(result[0]):
                        result.append(curr_list)
                    else:
                        break
            else:
                for i in range(len(curr)):
                    for j in range(26):
                        next_word = curr[:i] + chr(97 + j) + curr[i + 1:]
                        if next_word in wordList and next_word not in visited:
                            queue.append((next_word, curr_list, visited))
        return result


