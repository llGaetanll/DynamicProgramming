# Write a function `countConstruct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return the number of ways that the `target` can be
# constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed.



# m: target length
# n: word_bank length
#
# Time: O(mn^m)
# Space: O(m^2)
def count_construct(target, word_bank):
	if target == "": return 1

	count = 0
	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]

			if count_construct(suffix, word_bank) > 0:
				count += 1
	
	return count



# m: target length
# n: word_bank length
#
# Time: O(nm^2)
# Space: O(m^2)
def count_construct_memo(target, word_bank, memo = {}):
	if target == "": return 1

	if target in memo:
		return memo[target]

	count = 0
	for word in word_bank:
		if target.startswith(word):
			suffix = target[len(word):]

			if count_construct(suffix, word_bank) > 0:
				count += 1

	memo[target] = count
	
	return count


print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'abcdef']))
print(count_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))

print(count_construct_memo("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'abcdef']))
print(count_construct_memo("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))