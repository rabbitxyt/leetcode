# You are given a map in form of a two-dimensional integer grid where 1 represents land
# and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or
# more connected land cells). The island doesn't have "lakes" (water inside that isn't connected
# to the water around the island). One cell is a square with side length 1. The grid is rectangular,
# width and height don't exceed 100. Determine the perimeter of the island.


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        one = 0
        dup = 0

        for row in grid:
            one += row.count(1)

        for row in range(len(grid)):
            for col in range(len(grid[0]) - 1):
                if grid[row][col] == 1 and grid[row][col + 1] == 1:
                    dup += 1

        grid = list(map(list, zip(*grid)))

        for row in range(len(grid)):
            for col in range(len(grid[0]) - 1):
                if grid[row][col] == 1 and grid[row][col + 1] == 1:
                    dup += 1

        return (one * 4 - dup * 2)
