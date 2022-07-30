# Suppose that you are a traveler on a 2D grid. You begin in the top-left corner
# and you goal is to travel to the bottom-right corner. Youu may only move down
# or right.

# In how many ways can you travel to the goal on a grid with dimensions m * n?

# Write a function `gridTraveler(m, n)` that calculates this.



# m: rows
# n: columns
#
# Time: O(mn)
# Space: O(mn)
def grid_traveler(m, n):
	# fill a matrix of size (m + 1) x (n + 1) with zeroes
	# we add a row and column simply because of 0 indexing
	grid = [[0] * (n + 1) for _ in range(m + 1)]

	# there is only one way to travel through a 1x1 grid
	grid[1][1] = 1

	# each cell in the table adds its value to its right and bottom neighbor
	for i, row in enumerate(grid):
		for j, el in enumerate(row):

			# i is the row counter
			if i + 1 <= m:
				grid[i + 1][j] += el

			# j is the col counter
			if j + 1 <= n:
				grid[i][j + 1] += el

	return grid[m][n]



print(grid_traveler(18, 18))