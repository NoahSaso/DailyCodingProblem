def largest_sum(arr):
  largest = 0
  for idx, x in enumerate(arr):
    # create a second array of all values non-adjacent to this one
    # (non-adjacent values have index distances greater than 1)
    arr2 = [x2 for (idx2, x2) in enumerate(arr) if abs(idx - idx2) > 1]
    # find largest sum
    for x2 in arr2:
      s = x + x2
      if largest < s: largest = s
  return largest

# TODO: O(N) time and constant space

print(largest_sum([9, 4, 6, 8]))