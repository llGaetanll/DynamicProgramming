# Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an
# array of numbers as arguments.

# The function shoudl return an array containing any combination of elements
# that add up to exactly the targetSum. If there is no combination that adds up
# to the targetSum, then return null.

# If multiple solutions exist, you may return any of them.



# m: target sum
# n: array length
#
# Time: O(n^m * m)
#  Note that we are counting the time taken by the creation of the copy of
#  the array.
#
# Space: O(m)
def how_sum(targetSum, numbers):
	if targetSum == 0: return []
	if targetSum < 0: return None

	for number in numbers:
		val = targetSum - number

		res = how_sum(val, numbers)
		if res is not None:
			return [number, *res] # spread operator

	return None


# m: target sum
# n: array length
#
# Time: O(n * m^2)
# 	Note that we are counting the time taken by the creation of the copy of
#  	the array.
#
# Space: O(m^2)
#   There are m keys, which each have an array value of length m in the worst
#   case. 
def how_sum_memo(targetSum, numbers, memo = {}):
	if targetSum == 0: return []
	if targetSum < 0: return None

	if targetSum in memo:
		return memo[targetSum]

	for number in numbers:
		val = targetSum - number

		res = how_sum_memo(val, numbers, memo)
		if res is not None:
			memo[targetSum] = [number, *res]
			return memo[targetSum]

	memo[targetSum] = None
	return None



print(how_sum_memo(7, [5, 3, 4, 7]))
print(how_sum(7, [5, 3, 4, 7]))

print(how_sum_memo(300, [7, 14]))
print(how_sum(300, [7, 14]))