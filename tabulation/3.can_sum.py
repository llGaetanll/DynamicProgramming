# Write a function `can_sum(target_sum, numbers)` that takes in a target sum and
# an array of numbers as arguments.

# The function should return a boolean indicating whether or not it is possible
# to ghenerate thetarget sum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are non-negative.



# m: targetSum
# n: numbers length
#
# Time: O(mn)
# Space: O(m)
def can_sum(targetSum, numbers):
	# each index `i` of the list represents whether number `i` can be
	# generated using any number in `numbers`. We start off by assuming that no
	# quantity is reachable
	lst = [False] * (targetSum + 1)

	# it's always possible to generate 0, just do nothing
	lst[0] = True

	# iterate through the list
	for i in range(len(lst)):

		# if the current sum is unacheivable, don't build upon it
		if not lst[i]:
			continue

		# if the current index `i` can be reached, then any `i + k` can be reached
		# where `k` is any element of `numbers`
		for num in numbers:

			# only update list items which are reachable
			if i + num < len(lst):
				lst[i + num] = True

	return lst[targetSum]



print(can_sum(7, [3, 4, 5]))
print(can_sum(300, [7, 14]))