class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = collections.defaultdict(list)
        wordDict = set(wordDict)

        def find_sentences(sentence):

            if not sentence:
                return [[]]

            if sentence in memo:
                return memo[sentence]

            for sentence_end in range(1, len(sentence) + 1):
                current_word = sentence[:sentence_end]
                if current_word in wordDict:
                    sentence_breaks = find_sentences(sentence[sentence_end:])

                    for sentence_break in sentence_breaks:
                        memo[sentence].append([current_word] + sentence_break)

            return memo[sentence]

        find_sentences(s)
        return [" ".join(sentence) for sentence in memo[s]]