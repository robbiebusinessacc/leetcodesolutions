class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0  # Start from the bottom-left corner of the grid

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += n - col  # All elements to the right are also negative
                row -= 1  # Move up a row
            else:
                col += 1  # Move right in the row

        return count
