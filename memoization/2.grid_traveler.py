# Suppose that you are a traveler on a 2D grid. You begin in the top-left corner
# and your goal is to travel to the bottom-right corner. You may only move down
# or right.

# How many ways can you travel to the goal on a grid of size m * n



# Time: O(2^{n + m})
# Space: O(n + m), the height of the tree
def grid_traveler(m, n):
	# if one of the sidelengths is 0, it's not a grid
	if m < 1 or n < 1:
		return 0

	# there is only one way to get to the end: do nothing
	if m == 1 and n == 1:
		return 1

	return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)



# Time: O(m * n)
# Space: O(m + n)
def grid_traveler_memo(m, n, memo = {}):
	# if one of the sidelengths is 0, it's not a grid
	if m < 1 or n < 1:
		return 0

	# there is only one way to get to the end: do nothing
	if m == 1 and n == 1:
		return 1	

	key = f"{m},{n}"
	if key in memo:
		return memo[key]

	memo[key] = grid_traveler_memo(m - 1, n, memo) + grid_traveler_memo(m, n - 1, memo)
	return memo[key]

print(grid_traveler_memo(18, 18)) # 2333606220
# print(grid_traveler(18, 18)) # 2333606220