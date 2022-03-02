# Approach 2: Trie + Merged Intervals

# https://leetcode.com/problems/add-bold-tag-in-string/discuss/1035897/Python-both-version-(Trie-%2B-Merged-Intervals)-and-(Trie-%2B-mask)

# can also use 2 for loops to get windows and sort by start position

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution(object):
    def addBoldTag(self, s, words):
        self.trie = Trie()
        self.mergedIntervals = []
        
        for word in words:
            self.addToTrie(word)
        
        for i in range(len(s)):
            node = self.trie
            end = None
            
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.isWord:
                    end = j + 1
            
            if end:
                self.addToIntervals([i, end])
        
        res = []
        prevEnd = 0
        for start, end in self.mergedIntervals:
            res.append(s[prevEnd:start])
            res.append('<b>')
            res.append(s[start:end])
            res.append('</b>')
            prevEnd = end
        
        # if anything remaining
        res.append(s[prevEnd:])
        
        return ''.join(res)
    
    def addToIntervals(self, interval):
        if not self.mergedIntervals or self.mergedIntervals[-1][1] < interval[0]:
            self.mergedIntervals.append(interval)
        else:
            self.mergedIntervals[-1][-1] = max(self.mergedIntervals[-1][-1], interval[1])
    
    def addToTrie(self, word):
        node = self.trie
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        
        node.isWord = True