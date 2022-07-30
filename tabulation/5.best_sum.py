# Write a function `best_sum(target_sum, numbers)` that takes in a target sum
# and an array of numbers as arguments.

# The function should return an array containing the shortest combination of
# numbers that add up to exactly the target sum.

# If there is a tie for the shortest combination, you may return any one of
# them.



# m: targetSum
# n: numbers length
#
# Time: O(nm^2)
# Space: O(m^2)
def best_sum(targetSum, numbers):
	# each index `i` of the list represents whether number `i` can be
	# generated using any number in `numbers`. We start off by assuming that no
	# quantity is makeable
	lst = [None] * (targetSum + 1)

	# the best way to generate 0 is to just do nothing
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
			if i + num >= len(lst):
				continue

			# current sum to number `i + num`
			cur_sum = lst[i + num]

			# new contender sum to number `i + num`
			new_sum = [num, *lst[i]]

			# if there was previously no way of summing to `i + num`, now there is
			if cur_sum is None:
				lst[i + num] = new_sum

			# if the new contender sum to `i + num` is shorter than the current one, update it
			elif len(cur_sum) > len(new_sum):
				lst[i + num] = new_sum

	return lst[targetSum]



print(best_sum(8, [2, 3, 5]))
print(best_sum(100, [1, 2, 5, 25]))