# Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an
# array of numbers as arguments.

# The function should return a boolean indicating whether or not it is possible
# to generate the targetSum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are nonnegative.



# m: target sum
# n: numbers length
#
# Time: O(n^m)
# Space: O(m)
def can_sum(targetSum, numbers):
  if targetSum == 0: return True
  if targetSum < 0: return False 

  for number in numbers:
    val = targetSum - number

    if can_sum(val, numbers): return True

  return False


# m: target sum
# n: array length
#
# Time: O(m * n)
#   Since lookup is O(1), m * n represents all possible lookups of targetsums
#   and array length differences.
#
# Space: O(m)
# 	Since memo keys can range from [0, m], nothing more.
def can_sum_memo(targetSum, numbers, memo = {}):
  if targetSum == 0: return True
  if targetSum < 0: return False 

  for number in numbers:
    val = targetSum - number

    if val in memo:
      return memo[val]
    
    memo[val] = can_sum_memo(val, numbers, memo)

    if memo[val]: return True

  return False


print(can_sum_memo(7, [3, 4, 5]))
print(can_sum(7, [3, 4, 5]))

print(can_sum_memo(300, [7, 14]))
print(can_sum(300, [7, 14]))