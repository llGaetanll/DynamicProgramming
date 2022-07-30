# Write a function `canConstruct(target, word_bank)` that accepts a target string
# and an array of strings.

# The function should return a boolean indicating whether or not the `target`
# can be constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed.



# m: target length
# n: word_bank length
#
# Time: O(n^m * m)
# Size: O(m^2)
def can_construct(target, word_bank):
	if target == "": return True

	for word in word_bank:
		if target.startswith(word):
			val = target[len(word):]

			if can_construct(val, word_bank): return True
	
	return False


# m: target length
# n: word_bank length
#
# Time: O(n * m^2)
# Size: O(m^2)
def can_construct_memo(target, word_bank, memo = {}):
	if target == "": return True

	if target in memo:
		return memo[target]

	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]

			memo[target] = can_construct_memo(suffix, word_bank, memo)

			if memo[target]: return True
	
	return False

print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))

print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeee']))