"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return []
        wordList = set(wordList)
        queue = [(beginWord, [], set(), 0)]
        levels ={}
        while queue:
            curr, curr_list, visited, level = queue.pop(0)
            if curr in levels:
                if level > levels[curr]:
                    continue
            else:
                levels[curr] = level
            curr_list = curr_list + [curr]
            visited.add(curr)
            if curr == endWord:
                return len(curr_list)
            else:
                for i in range(len(curr)):
                    for j in range(26):
                        next_word = curr[:i]+chr(97+j)+curr[i+1:]
                        if next_word in wordList and next_word not in visited:
                            queue.append((next_word, curr_list, visited, level+1))
        return 0
