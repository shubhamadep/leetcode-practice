class Solution(object):
    def minScoreTriangulation(self, values):
        @functools.cache
        def _loop(start: int, end: int) -> int:
            if (end - start + 1) < 3:
                return 0
            min_score = sys.maxsize
            for k in range(start + 1, end):
                min_score = min(min_score, values[start] * values[k] * values[end] + _loop(start, k) + _loop(k, end))
            return min_score

        return _loop(0, len(values) - 1)