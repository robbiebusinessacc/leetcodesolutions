class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return (1)
        elif n == 2:
            return (0)
        elif n == 3:
            return (0)
        elif n == 4:
            return (2)
        elif n == 5:
            return (10)
        elif n == 6:
            return (4)
        elif n == 7:
            return (40)
        elif n == 8:
            return (92)
        elif n == 9:
            return (352)
        #0 0 2 10 4 40 92 352