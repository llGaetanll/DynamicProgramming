# Write a funciton `fib(n` that takes in a number as an argument. The function
# should return the n-th number of the Fibonacci sequence.

# The 0th number of the sequence is 0.  The 1st number of the sequence is 1.

# To generate the next numberof the sequence, we sum the previous two.


# Solve this itteratively using a table, instead of recursively



# Time: O(n)
# Space: O(n)
def fib(n):
  # fill a list of size n + 1 with zeroes
  lst = [0] * (n + 1)

  # fib(1) = 1
  lst[1] = 1

  # each index adds its value to its neighbor and next-neighbor
  for i, el in enumerate(lst):
    # add to neighbor
    if i + 1 < len(lst):
      lst[i + 1] += el

    # add to next-neighbor
    if i + 2 < len(lst):
      lst[i + 2] += el

  return lst[n]



print(fib(50))