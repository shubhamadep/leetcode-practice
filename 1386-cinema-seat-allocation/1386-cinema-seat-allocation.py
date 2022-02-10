class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = dict()
        for row, col in reservedSeats:
            if row in reserved:
                reserved[row].add(col)
            else:
                reserved[row] = set([col])
        groups = 0
        for r, set_reserved in reserved.items():
            if not set_reserved & {2, 3, 4, 5}:
                groups += 1
                if not set_reserved & {6, 7, 8, 9}:
                    groups += 1
            elif not set_reserved & {6, 7, 8, 9}:
                groups += 1
            elif not set_reserved & {4, 5, 6, 7}:
                groups += 1
        #empty rows which do not exist in the reserved dict()
        return groups + (n - len(reserved)) * 2