# Write a function `bestSum(targetSum, numbers)` that takes in a targetSum and
# an array of numbers as arguments.

# The function should return a array containgn the shortest combination of
# numbers that add up to exactly the targetSum.

# If there is a tie for the shortest combination, you may return any oe of the
# shortest.



# m: target sum
# n: array length
#
# Time: O(n^m * m)
# Space: O(m^2)
def best_sum(targetSum, numbers):
  if targetSum == 0: return []
  if targetSum < 0: return None

  best = None # best is the shortest sum of all children
  for number in numbers:
    val = targetSum - number

    res = best_sum(val, numbers)
    if res is not None and (best is None or len(best) > len(res)):
      best = [number, *res]

  return best


# Time: O(n * m^2)
# Space: O(m^2)
def best_sum_memo(targetSum, numbers, memo = {}):
  if targetSum == 0: return []
  if targetSum < 0: return None

  if targetSum in memo:
    return memo[targetSum]

  best = None # best is the shortest sum of all children
  for number in numbers:
    val = targetSum - number

    res = best_sum_memo(val, numbers, memo)
    if res is not None and (best is None or len(best) > len(res)):
      best = [number, *res]

  memo[targetSum] = best

  return best



print(best_sum_memo(8, [2, 3, 5]))
print(best_sum(8, [2, 3, 5]))

print(best_sum_memo(100, [1, 2, 5, 25]))
print(best_sum(100, [1, 2, 5, 25]))