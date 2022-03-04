class Solution:
    def longestValidParentheses(self, string: str) -> int:
        ob, cb = 0, 0
        max_valid = 0

        for char in string:
            if char == '(':
                ob += 1
            else:
                cb += 1

            if ob == cb:
                max_valid = max(max_valid, cb*2)
            elif cb > ob:
                ob = 0
                cb = 0

        ob, cb = 0, 0

        for i in reversed(range(len(string))):
            char = string[i]
            if char == '(':
                ob += 1
            else:
                cb += 1

            if ob == cb:
                max_valid = max(max_valid, ob*2)
            elif ob > cb:
                ob = 0
                cb = 0

        return max_valid