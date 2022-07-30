# Write a function `can_construct(target, word_bank)` that accepts a target string
# and an array of strings.

# The function should return a boolean indicating whether or not the `target`
# can be constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed.



# m: target length
# n: word_bank length
#
# Time:
# Size:
def can_construct(target, word_bank):
	# each index `i` of the list represents whether the string `target[i:]` can be
	# generated using any word in `word_bank`. We start off by assuming that no
	# string is reachable
	lst = [False] * (len(target) + 1)

	# it's always possible to generate "", just do nothing
	lst[0] = True

	# iterate through the list
	for i in range(len(lst)):

		# if the current sum is unacheivable, don't build upon it
		if not lst[i]:
			continue

		for word in word_bank:

			if target[i:].startswith(word):
				lst[i + len(word)] = True

	return lst[len(target)]



print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))