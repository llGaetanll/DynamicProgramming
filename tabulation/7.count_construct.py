# Write a function `count_construct(target, word_bank)` that accepts a target
# string and an array of strings.

# The function should return the number of ways that the `target` can be
# constructed by concatenating elements of the `word_bank` array.

# You may reuse elements of `word_bank` as many times as needed.



def count_construct(target, word_bank):
  lst = [0] * (len(target) + 1)

  # there is only one way to construct the empty string: do nothing
  lst[0] = 1

  for i, el in enumerate(lst):

    # if we can't construct index i, skip
    if el == 0:
      continue

    sub_target = target[i:]

    for word in word_bank:

      # only update list items which match the rest of the string
      if not sub_target.startswith(word):
        continue

      idx = i + len(word)

      if lst[idx] is None:
        lst[idx] = 1
      else:
        lst[idx] += 1

    print(i, lst)

  
  return lst[len(target)]

print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'abcdef']))
print(count_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
