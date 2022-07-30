# Write a function `all_construct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return an 2D array containing all of the ways that the
# `target` can be constructed by concatenating elements of the `word_bank`
# array. Each element of the 2D array should represent ond combination that
# construct the `target`.

# You may reuse elements of `word_bank` as many times as needed.



def all_construct(target, word_bank):
	lst = [None] * (len(target) + 1)

	# only one way to construct the empty string: it's just doing nothing
	lst[0] = [[]]

	for i, el in enumerate(lst):

		# if we can't construct the current string, skip
		if el is None:
			continue

		for word in word_bank:
			sub_target = target[i:]

			if not sub_target.startswith(word):
				continue

			lst[i + len(word)] = [word, *el]
	
	return lst
			


print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))