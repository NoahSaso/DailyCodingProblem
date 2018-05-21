# the best way to find if any two numbers in a list sum to a number
# is by finding the difference between the sum and one of the numbers,
# then just seeing if that difference exists elsewhere
# (using a set is more efficient when searching with 'in' multiple times)
def sums_to_k(nums, k):
  snums = set(nums)
  for n in snums:
    if k - n in snums: return True
  return False

l = [1, 4, 6, 2, 10]
print(sums_to_k(l, 13), sums_to_k(l, 12))