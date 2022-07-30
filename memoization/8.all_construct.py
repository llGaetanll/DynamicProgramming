# Write a function `allConstruct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return an 2D array containing all of the ways that the
# `target` can be constructed by concatenating elements of the `word_bank`
# array. Each element of the 2D array should represent ond combination that
# construct the `target`.

# You may reuse elements of `word_bank` as many times as needed.



# m: target length
# n: word_bank length
#
# Time: O(n^m)
# Space: O(m)
#  	The height of the recursion tree. Here we don't count the length of the
#  	output, otherwise it would also be exponential in space.
def all_construct(target, word_bank):
	if target == "": return [[]]

	ways = []
	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]

			results = all_construct(suffix, word_bank)

			for res in results:
				res.insert(0, word)

			ways.extend(results)

	return ways


# Note that this memoized function is no better than the first approach.
# m: target length
# n: word_bank length
#
# Time: O(n^m)
# Space: O(m)
def all_construct_memo(target, word_bank, memo = {}):
	if target == "": return [[]]

	if target in memo:
		return memo[target]

	ways = []
	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]

			results = all_construct_memo(suffix, word_bank, memo)

			for res in results:
				res.insert(0, word)

			ways.extend(results)

	target[memo] = ways

	return ways


print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))