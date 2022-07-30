# Write a function fib(n) that returns the nth number of the fibonacci sequence



# Time: O(2^n)
# Space: O(n)
def fib(n):
  if n <= 2:
    return 1

  return fib(n - 1) + fib(n - 2)


# Time: O(n)
# Space: O(n)
def fib_memo(n, memo = {}):
  if n <= 2:
    return 1

  if n in memo:
    return memo[n]

  memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

  return memo[n]

print(fib_memo(50))
print(fib(50))