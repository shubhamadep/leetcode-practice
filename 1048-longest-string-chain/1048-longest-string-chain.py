class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = lambda x: len(x))
        ans = 1
        hashmap = dict()
        for w in words:
            hashmap[w] = 1
        
        for w in words:
            x = 1
            for i in range(len(w)):
                temp = w[:i] + w[i + 1:]
                prev = hashmap.get(temp, 0)
                x = max(x, prev + 1)
            hashmap[w] = x
            ans = max(ans, x)
        return ans