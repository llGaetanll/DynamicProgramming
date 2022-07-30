# Write a function `how_sum(target_sum, numbers)` that takes in a target sum and
# an array of numbers as arguments.

# The function should return an array containing any combination of elements
# that add up to exactly the target sum.

# If there is no combination that adds up to the target sum, then return None.

# If there are multiple combinations possible, you may return any single one.



# m: targetSum
# n: numbers length
#
# Time: O(nm^2)
# Space: O(m^2)
def how_sum(targetSum, numbers):
	# each index `i` of the list represents whether number `i` can be
	# generated using any number in `numbers`. We start off by assuming that no
	# quantity is makeable
	lst = [None] * (targetSum + 1)

	# it's always possible to generate 0, just do nothing
	lst[0] = []

	# iterate through the list
	for i in range(len(lst)):

		# if the current sum is unacheivable, don't build upon it
		if lst[i] is None:
			continue

		# if the current index `i` can be reached, then any `i + k` can be reached
		# where `k` is any element of `numbers`
		for num in numbers:

			# only update list items which are reachable
			if i + num < len(lst):

				# "append" num to lst[i + num]'s list
				# note that this may not be the best (shortest) sum
				if lst[i + num] is None:
					lst[i + num] = [num]
				else:
					lst[i + num] = [num, *lst[i]] 

	return lst[targetSum]



print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(300, [7, 14]))